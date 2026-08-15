"""
ShadBot Agent Platform

Multi-module response splitting.

Purpose:
    LLMs asked for one module routinely answer with SEVERAL modules in a
    single response, delimited by a path comment:

        # src/agentplatform/domain/models.py
        @dataclass
        class Agent: ...

        # src/agentplatform/domain/services.py
        from .models import Agent

    Writing that blob into one file produces a syntactically valid file whose
    imports can never resolve (`from .models import Agent` when models.py was
    never written). That is exactly how ShadBotCore_BuiltByAgent ended up with
    14 files of which 0 were importable and 7 were byte-identical.

Responsibility:
    Detect those delimiters and split one response into (relative_path, code)
    pairs so each module lands at its declared path.

Dependencies:
    Standard library only (ast, re).

Design rules honoured:
    - Rule 27: no fake implementations. If no delimiter is found the input is
      returned unchanged as a single unit rather than guessed at.
    - Rule 18: failures are reported, not swallowed.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass

# A path delimiter comment on its own line:
#     # src/agentplatform/domain/models.py
#     # File: src/foo/bar.py
#     # --- src/foo/bar.py ---
_PATH_COMMENT = re.compile(
    r"""^[ \t]*\#[ \t]*
        (?:-{2,}[ \t]*)?
        (?:file[ \t]*:[ \t]*|path[ \t]*:[ \t]*)?
        (?P<path>
            (?:[A-Za-z0-9_.\-]+/)*
            [A-Za-z0-9_.\-]+\.py
        )
        [ \t]*
        (?:-{2,})?
        [ \t]*$
    """,
    re.VERBOSE | re.MULTILINE | re.IGNORECASE,
)

# Paths we must never write to, regardless of what the model claims.
_FORBIDDEN_SEGMENTS = frozenset({"..", "~"})


@dataclass(frozen=True, slots=True)
class SplitModule:
    """
    One module extracted from a multi-module response.
    """

    path: str

    content: str

    @property
    def is_parseable(self) -> bool:
        """
        Whether the extracted content is valid Python.
        """

        try:
            ast.parse(self.content)
        except SyntaxError:
            return False

        return True


class ModuleSplitter:
    """
    Splits a multi-module LLM response into individual modules.
    """

    def split(
        self,
        code: str,
        default_path: str,
    ) -> list[SplitModule]:
        """
        Split `code` into modules.

        Args:
            code: Raw code extracted from the LLM response.
            default_path: Path to use when the response contains no
                delimiters, i.e. the module the agent actually asked for.

        Returns:
            One SplitModule per detected module. Never empty: a response with
            no delimiters yields a single module at `default_path`.
        """

        if not code.strip():
            return [SplitModule(path=default_path, content=code)]

        matches = list(_PATH_COMMENT.finditer(code))

        if not matches:
            return [SplitModule(path=default_path, content=code)]

        modules: list[SplitModule] = []

        # Content before the first delimiter (imports, module docstring) is
        # prepended to the first module rather than discarded.
        preamble = code[: matches[0].start()].strip()

        for index, match in enumerate(matches):
            start = match.end()
            end = (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(code)
            )

            body = code[start:end].strip()

            if index == 0 and preamble:
                body = f"{preamble}\n\n{body}".strip()

            if not body:
                continue

            path = self._sanitise(match.group("path"))

            if path is None:
                continue

            modules.append(
                SplitModule(path=path, content=body + "\n"),
            )

        if not modules:
            return [SplitModule(path=default_path, content=code)]

        return self._propagate_shared_imports(
            self._merge_duplicates(modules),
        )

    @staticmethod
    def _sanitise(raw: str) -> str | None:
        """
        Reject path traversal and absolute paths.

        Returns None when the path is unsafe.
        """

        path = raw.strip().replace("\\", "/").lstrip("/")

        if not path.endswith(".py"):
            return None

        segments = [s for s in path.split("/") if s]

        if any(segment in _FORBIDDEN_SEGMENTS for segment in segments):
            return None

        if not segments:
            return None

        return "/".join(segments)

    @staticmethod
    def _merge_duplicates(
        modules: list[SplitModule],
    ) -> list[SplitModule]:
        """
        Concatenate modules that declare the same path.

        A model occasionally emits the same path twice (e.g. adding methods to
        a class it defined earlier). Concatenating is closer to intent than
        letting the later block silently overwrite the earlier one.
        """

        ordered: list[str] = []
        merged: dict[str, list[str]] = {}

        for module in modules:
            if module.path not in merged:
                merged[module.path] = []
                ordered.append(module.path)

            merged[module.path].append(module.content.rstrip())

        return [
            SplitModule(
                path=path,
                content="\n\n".join(merged[path]) + "\n",
            )
            for path in ordered
        ]

    @staticmethod
    def _propagate_shared_imports(
        modules: list[SplitModule],
    ) -> list[SplitModule]:
        """
        Re-add stdlib imports the model declared only once.

        When a model emits several modules in one response it typically writes
        `from typing import List` at the very top and then uses `List` in every
        subsequent module. Once split, those later modules raise NameError.

        This collects absolute (non-relative) imports from all modules and
        prepends the ones a module actually references but does not import.
        Only names genuinely used are added, so no unused imports appear.
        """

        if len(modules) < 2:
            return modules

        # name -> import statement that binds it
        available: dict[str, str] = {}

        for module in modules:
            try:
                tree = ast.parse(module.content)
            except SyntaxError:
                continue

            for node in tree.body:
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        bound = alias.asname or alias.name.split(".")[0]
                        available.setdefault(bound, f"import {alias.name}")
                        if alias.asname:
                            available[bound] = f"import {alias.name} as {alias.asname}"

                elif isinstance(node, ast.ImportFrom):
                    # Relative imports are module-specific; never propagate.
                    if node.level:
                        continue
                    if node.module is None:
                        continue
                    for alias in node.names:
                        if alias.name == "*":
                            continue
                        bound = alias.asname or alias.name
                        statement = f"from {node.module} import {alias.name}"
                        if alias.asname:
                            statement += f" as {alias.asname}"
                        available.setdefault(bound, statement)

        if not available:
            return modules

        repaired: list[SplitModule] = []

        for module in modules:
            try:
                tree = ast.parse(module.content)
            except SyntaxError:
                repaired.append(module)
                continue

            bound: set[str] = set()
            used: set[str] = set()

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        bound.add(alias.asname or alias.name.split(".")[0])
                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        bound.add(alias.asname or alias.name)
                elif isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                    bound.add(node.name)
                elif isinstance(node, ast.Name):
                    if isinstance(node.ctx, ast.Store):
                        bound.add(node.id)
                    else:
                        used.add(node.id)
                elif isinstance(node, ast.Attribute):
                    root = node
                    while isinstance(root, ast.Attribute):
                        root = root.value  # type: ignore[assignment]
                    if isinstance(root, ast.Name):
                        used.add(root.id)

            missing = sorted(
                name
                for name in used - bound
                if name in available
            )

            if not missing:
                repaired.append(module)
                continue

            header = "\n".join(available[name] for name in missing)

            repaired.append(
                SplitModule(
                    path=module.path,
                    content=f"{header}\n\n{module.content.lstrip()}",
                ),
            )

        return repaired
