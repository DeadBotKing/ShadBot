"""
ShadBot Agent Platform

Code generation service.
"""

from __future__ import annotations

import ast
from dataclasses import replace
from pathlib import Path

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.generation.artifact_service import (
    ArtifactService,
)
from agentplatform.application.generation.module_splitter import (
    ModuleSplitter,
)
from agentplatform.application.prompt.prompt_builder import (
    CODEGEN_FILE_KEY,
    CODEGEN_PURPOSE_KEY,
    CODEGEN_SIBLINGS_KEY,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.artifacts import (
    ArtifactType,
    GeneratedArtifact,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.infrastructure.tools import (
    CodeExtractor,
)


class CodeGenerationService:
    """
    Generates source code artifacts.
    """

    def __init__(
        self,
        brain: AgentBrain,
        extractor: CodeExtractor | None = None,
        artifact_service: ArtifactService | None = None,
        splitter: ModuleSplitter | None = None,
        project_root: Path | None = None,
    ) -> None:
        self._brain = brain
        self._extractor = extractor or CodeExtractor()
        self._artifact_service = artifact_service or ArtifactService()
        self._splitter = splitter or ModuleSplitter()
        self._project_root = project_root

    def generate(
        self,
        context: AgentExecutionContext,
        file_path: Path,
        instructions: str,
        purpose: str = "",
        sibling_files: tuple[str, ...] = (),
    ) -> GeneratedArtifact:
        """
        Generate and persist source file.

        Args:
            context: Execution context.
            file_path: Absolute path of the module to write.
            instructions: Legacy free-text instructions.
            purpose: The single responsibility of this module. Drives the
                focused per-file prompt.
            sibling_files: Other modules in the project, so the model imports
                them instead of re-implementing them in this file.
        """

        root = self._resolve_root(file_path)

        relative_target = self._relative_to_root(file_path, root)

        # Switch PromptBuilder into focused single-file mode. Without this the
        # prompts for different modules were 96.4% identical and the model
        # returned the same response for every file.
        generation_context = replace(
            context,
            instructions=instructions,
            metadata={
                **context.metadata,
                CODEGEN_FILE_KEY: relative_target,
                CODEGEN_PURPOSE_KEY: purpose or instructions,
                CODEGEN_SIBLINGS_KEY: [
                    path for path in sibling_files if path != relative_target
                ],
            },
        )

        response = self._brain.think(
            AgentRole.ENGINEER,
            generation_context,
        )

        code = self._extractor.extract(
            response,
        )

        modules = self._splitter.split(
            code=code,
            default_path=self._relative_to_root(file_path, root),
        )

        primary: GeneratedArtifact | None = None
        written: list[Path] = []

        for module in modules:
            target = (root / module.path).resolve()

            # Never escape the project root, whatever the model emitted.
            if not self._is_within(target, root):
                print(
                    f"[CODE GENERATION] Rejected out-of-tree module path: "
                    f"{module.path}",
                )
                continue

            artifact = GeneratedArtifact(
                path=target,
                content=module.content,
                artifact_type=ArtifactType.SOURCE_CODE,
            )

            self._artifact_service.save(
                artifact,
            )

            written.append(target)

            if primary is None or target == file_path.resolve():
                primary = artifact

        if len(modules) > 1:
            print(
                f"[CODE GENERATION] Split response into {len(written)} module(s): "
                + ", ".join(str(p.relative_to(root)) for p in written),
            )

        # The model sometimes answers a request for file A with content it
        # labels as file B, so the planned module is silently never written.
        # Run 3 lost domain/agents/agent_role.py this way: AgentRole ended up
        # inside agent_contract.py and five modules then failed to import
        # "agentplatform.domain.agents.agent_role".
        requested = file_path.resolve()

        if requested not in written and self._is_within(requested, root):
            print(
                f"[CODE GENERATION] Model did not emit the requested file "
                f"{relative_target}; writing a re-export shim so planned "
                f"imports resolve.",
            )

            shim = self._build_shim(
                requested=requested,
                written=written,
                root=root,
            )

            shim_artifact = GeneratedArtifact(
                path=requested,
                content=shim,
                artifact_type=ArtifactType.SOURCE_CODE,
            )

            self._artifact_service.save(shim_artifact)

            written.append(requested)

            if primary is None:
                primary = shim_artifact

        self._ensure_packages(written, root)

        if primary is None:
            # Every candidate path was rejected: persist at the requested path
            # rather than silently producing nothing.
            primary = GeneratedArtifact(
                path=file_path,
                content=code,
                artifact_type=ArtifactType.SOURCE_CODE,
            )

            self._artifact_service.save(
                primary,
            )

        return primary

    def _build_shim(
        self,
        requested: Path,
        written: list[Path],
        root: Path,
    ) -> str:
        """
        Build a module that re-exports symbols the model put elsewhere.

        The planned module name is what the rest of the generated project
        imports. If the model wrote those symbols into a different file, a
        re-export keeps the planned import path working instead of leaving a
        hole that breaks every dependent module.

        When nothing suitable is found the shim raises NotImplementedError:
        an honest failure, never a silent empty module that would let the
        gate pass.
        """

        expected_symbol = "".join(
            part.capitalize() for part in requested.stem.split("_")
        )

        for candidate in written:
            try:
                source = candidate.read_text(encoding="utf-8")
                tree = ast.parse(source)
            except (OSError, SyntaxError):
                continue

            names = [
                node.name
                for node in tree.body
                if isinstance(node, (ast.ClassDef, ast.FunctionDef))
            ]

            match = next(
                (name for name in names if name.lower() == expected_symbol.lower()),
                None,
            )

            if match is None:
                continue

            module_path = self._module_path(candidate, root)

            return (
                f'"""Re-export of {match}.\n\n'
                f"The generator emitted {match} into "
                f"{self._relative_to_root(candidate, root)} instead of this\n"
                f"module. This shim preserves the planned import path.\n"
                f'"""\n\n'
                f"from {module_path} import {match}\n\n"
                f'__all__ = ["{match}"]\n'
            )

        return (
            f'"""Placeholder for {requested.name}.\n\n'
            f"The code generator did not produce this planned module.\n"
            f'"""\n\n\n'
            f"raise NotImplementedError(\n"
            f'    "{requested.name} was planned but never generated. "\n'
            f'    "Re-run the engineer agent for this module."\n'
            f")\n"
        )

    def _module_path(
        self,
        path: Path,
        root: Path,
    ) -> str:
        """
        Dotted import path for a written module.
        """

        relative = self._relative_to_root(path, root)

        if relative.endswith(".py"):
            relative = relative[: -len(".py")]

        parts = [part for part in relative.split("/") if part]

        if parts and parts[0] in {"src", "lib", "source"}:
            parts = parts[1:]

        if parts and parts[-1] == "__init__":
            parts = parts[:-1]

        return ".".join(parts)

    def _resolve_root(
        self,
        file_path: Path,
    ) -> Path:
        """
        Determine the project root that split paths are relative to.
        """

        if self._project_root is not None:
            return self._project_root.resolve()

        resolved = file_path.resolve()

        # Split paths are conventionally rooted at the directory containing
        # `src/`, so walk up past it when present.
        for parent in resolved.parents:
            if parent.name == "src":
                return parent.parent

        return resolved.parent

    @staticmethod
    def _relative_to_root(
        file_path: Path,
        root: Path,
    ) -> str:
        """
        Express the requested file path relative to the project root.
        """

        resolved = file_path.resolve()

        try:
            return str(resolved.relative_to(root)).replace("\\", "/")
        except ValueError:
            return resolved.name

    @staticmethod
    def _is_within(
        target: Path,
        root: Path,
    ) -> bool:
        """
        Whether `target` lives inside `root`.
        """

        try:
            target.relative_to(root)
        except ValueError:
            return False

        return True

    def _ensure_packages(
        self,
        written: list[Path],
        root: Path,
    ) -> None:
        """
        Create missing __init__.py files.

        Generated code uses relative imports (`from .models import Agent`),
        which cannot resolve without package markers. The agent never emits
        them, so the platform must.
        """

        created = 0

        for path in written:
            directory = path.parent

            while self._within(directory, root):
                marker = directory / "__init__.py"

                if not marker.exists():
                    marker.parent.mkdir(parents=True, exist_ok=True)
                    marker.write_text(
                        '"""Package marker generated by ShadBot."""\n',
                        encoding="utf-8",
                    )
                    created += 1

                if directory == root:
                    break

                directory = directory.parent

        if created:
            print(f"[CODE GENERATION] Created {created} missing __init__.py file(s).")

    @staticmethod
    def _within(
        directory: Path,
        root: Path,
    ) -> bool:
        """
        Whether `directory` is inside `root`, excluding the `src` dir itself.
        """

        if directory == root:
            return False

        try:
            relative = directory.relative_to(root)
        except ValueError:
            return False

        parts = relative.parts

        # `src/` is a source root, not a package.
        return bool(parts) and parts != ("src",)
