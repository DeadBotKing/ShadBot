"""
ShadBot Agent Platform

Code generation service.
"""

from __future__ import annotations

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
    ) -> GeneratedArtifact:
        """
        Generate and persist source file.
        """

        generation_context = replace(
            context,
            instructions=instructions,
        )

        response = self._brain.think(
            AgentRole.ENGINEER,
            generation_context,
        )

        code = self._extractor.extract(
            response,
        )

        root = self._resolve_root(file_path)

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
