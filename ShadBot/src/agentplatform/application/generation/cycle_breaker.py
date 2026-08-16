"""
ShadBot Agent Platform

Import cycle detection and repair.

Purpose:
    LLMs generating a multi-module project routinely create mutual imports:

        agent_orchestrator.py  imports  PlatformService
        platform_service.py    imports  AgentOrchestrator

    Python cannot load either module. Run 4 of ShadBotCore_BuiltByAgent lost
    6 of 11 modules to a single such cycle, all reporting
    "cannot import name 'AgentOrchestrator'".

Responsibility:
    Detect cycles in the generated package and repair the ones that are
    safely repairable: an import used ONLY inside type annotations can move
    under `if TYPE_CHECKING:` with `from __future__ import annotations`,
    which is the standard Python answer to this exact problem.

    A cycle whose imports are used at runtime is NOT rewritten - that would
    hide a genuine design flaw. It is reported so the gate can fail.

Dependencies:
    Standard library only (ast, collections, pathlib).

Design rules honoured:
    - Rule 27: no fake implementations. Unrepairable cycles are reported,
      never silently patched.
    - Rule 18: failures are reported, not swallowed.
"""

from __future__ import annotations

import ast
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

_SKIP_DIRECTORIES = frozenset(
    {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        "build",
        "dist",
    }
)


@dataclass(frozen=True, slots=True)
class CycleRepair:
    """
    One import moved behind TYPE_CHECKING to break a cycle.
    """

    module: str

    moved_import: str

    partner: str


class ImportCycleBreaker:
    """
    Finds import cycles and repairs the type-annotation-only ones.
    """

    def __init__(self, source_root: Path) -> None:
        self._root = Path(source_root)

    # -- public API ------------------------------------------------------

    def repair(
        self,
        max_passes: int = 20,
    ) -> tuple[list[CycleRepair], list[tuple[str, ...]]]:
        """
        Repair what can be repaired, iterating to a fixed point.

        Breaking one edge changes the graph, and cycles overlap: a single
        pass leaves most of a tangled cluster intact. Each pass therefore
        rebuilds the graph from the rewritten files and repeats until no
        cycle can be broken.

        Returns:
            (repairs applied, cycles that remain unrepaired)
        """

        repairs: list[CycleRepair] = []
        unrepaired: list[tuple[str, ...]] = []

        for _ in range(max_passes):
            graph, files = self._build_graph()

            cycles = self._find_cycles(graph)

            if not cycles:
                return repairs, []

            progressed = False
            unrepaired = []

            for cycle in cycles:
                applied = False

                # Break the cycle at any edge whose import is only used in
                # annotations.
                for index, module in enumerate(cycle):
                    partner = cycle[(index + 1) % len(cycle)]

                    path = files.get(module)

                    if path is None:
                        continue

                    repair = self._move_to_type_checking(path, module, partner)

                    if repair is not None:
                        repairs.append(repair)
                        applied = True
                        progressed = True
                        break

                if not applied:
                    unrepaired.append(cycle)

            if not progressed:
                break

        # Report only what is still cyclic after the final rewrite, not the
        # snapshot from the last pass.
        graph, _ = self._build_graph()

        return repairs, self._find_cycles(graph)

    # -- graph construction ----------------------------------------------

    def _build_graph(
        self,
    ) -> tuple[dict[str, set[str]], dict[str, Path]]:
        graph: dict[str, set[str]] = defaultdict(set)
        files: dict[str, Path] = {}

        for path in sorted(self._root.rglob("*.py")):
            if any(part in _SKIP_DIRECTORIES for part in path.parts):
                continue

            module = self._module_name(path)

            if not module:
                continue

            files[module] = path

            try:
                tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
            except (OSError, SyntaxError):
                continue

            # Imports guarded by TYPE_CHECKING, or living inside a function
            # or __main__ block, do not execute at import time and cannot
            # cause a cycle. Only module-level runtime imports count.
            deferred: set[int] = set()

            for node in ast.walk(tree):
                is_deferred_scope = (
                    isinstance(node, ast.If)
                    and isinstance(node.test, ast.Name)
                    and node.test.id == "TYPE_CHECKING"
                ) or isinstance(
                    node, (ast.FunctionDef, ast.AsyncFunctionDef)
                )

                if is_deferred_scope:
                    for inner in ast.walk(node):
                        deferred.add(id(inner))

            for block in self._main_blocks(tree):
                for inner in ast.walk(block):
                    deferred.add(id(inner))

            for node in ast.walk(tree):
                if id(node) in deferred:
                    continue
                if isinstance(node, ast.ImportFrom) and node.module and not node.level:
                    graph[module].add(node.module)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        graph[module].add(alias.name)

        # Keep only edges between modules that exist in this project.
        known = set(files)

        return (
            {
                module: {dep for dep in deps if dep in known}
                for module, deps in graph.items()
            },
            files,
        )

    def _module_name(self, path: Path) -> str:
        relative = path.relative_to(self._root).with_suffix("")

        parts = list(relative.parts)

        if parts and parts[-1] == "__init__":
            parts = parts[:-1]

        return ".".join(parts)

    # -- cycle detection --------------------------------------------------

    @staticmethod
    def _find_cycles(graph: dict[str, set[str]]) -> list[tuple[str, ...]]:
        """
        Return simple cycles found by depth-first search.
        """

        cycles: list[tuple[str, ...]] = []
        seen_signatures: set[frozenset[str]] = set()

        visiting: list[str] = []
        on_stack: set[str] = set()
        finished: set[str] = set()

        def visit(node: str) -> None:
            if node in finished:
                return

            if node in on_stack:
                start = visiting.index(node)
                cycle = tuple(visiting[start:])
                signature = frozenset(cycle)

                if signature not in seen_signatures:
                    seen_signatures.add(signature)
                    cycles.append(cycle)

                return

            visiting.append(node)
            on_stack.add(node)

            for dependency in sorted(graph.get(node, ())):
                visit(dependency)

            visiting.pop()
            on_stack.discard(node)
            finished.add(node)

        for node in sorted(graph):
            visit(node)

        return cycles

    # -- repair -----------------------------------------------------------

    def _move_to_type_checking(
        self,
        path: Path,
        module: str,
        partner: str,
    ) -> CycleRepair | None:
        """
        Move `from partner import X` under TYPE_CHECKING, if X is only used
        in annotations.

        Returns None when the import is used at runtime, because rewriting
        it would break the code instead of fixing it.
        """

        try:
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source)
        except (OSError, SyntaxError):
            return None

        target: ast.ImportFrom | None = None

        for node in tree.body:
            if (
                isinstance(node, ast.ImportFrom)
                and node.module == partner
                and not node.level
            ):
                target = node
                break

        if target is None:
            return None

        imported = [alias.asname or alias.name for alias in target.names]

        if not imported:
            return None

        if any(self._used_at_runtime(tree, name) for name in imported):
            return None

        # The name may still be used inside `if __name__ == "__main__":`.
        # That block never runs at import time, so the cycle is real only
        # for scripts. Keep those call sites working with a local import.
        needed_by_main = any(self._used_in_main_block(tree, name) for name in imported)

        lines = source.splitlines()

        start = target.lineno - 1
        end = target.end_lineno or target.lineno

        statement = "\n".join(lines[start:end]).strip()

        # Keep the __main__ demo working: re-import locally inside the guard,
        # where the module is fully loaded and the cycle no longer applies.
        if needed_by_main:
            for block_node in reversed(self._main_blocks(tree)):
                body_start = block_node.body[0].lineno - 1
                indent = " " * (len(lines[body_start]) - len(lines[body_start].lstrip()))
                lines.insert(body_start, f"{indent}{statement}")

            # Re-locate the import statement, which may have shifted down.
            start = next(
                index
                for index, line in enumerate(lines)
                if line.strip() == statement.splitlines()[0].strip()
            )
            end = start + (end - (target.lineno - 1))

        del lines[start:end]

        block = [
            "if TYPE_CHECKING:",
            f"    {statement}",
        ]

        insert_at = self._annotations_import_index(lines)

        lines[insert_at:insert_at] = ["", *block]

        rebuilt = "\n".join(lines)

        rebuilt = self._ensure_prelude(rebuilt)

        path.write_text(rebuilt.rstrip() + "\n", encoding="utf-8")

        return CycleRepair(
            module=module,
            moved_import=", ".join(imported),
            partner=partner,
        )

    @staticmethod
    def _main_blocks(tree: ast.AST) -> list[ast.If]:
        """
        Every `if __name__ == "__main__":` statement in the module.
        """

        blocks: list[ast.If] = []

        for node in ast.walk(tree):
            if not isinstance(node, ast.If):
                continue

            test = node.test

            if (
                isinstance(test, ast.Compare)
                and isinstance(test.left, ast.Name)
                and test.left.id == "__name__"
                and len(test.comparators) == 1
                and isinstance(test.comparators[0], ast.Constant)
                and test.comparators[0].value == "__main__"
            ):
                blocks.append(node)

        return blocks

    @classmethod
    def _used_in_main_block(cls, tree: ast.AST, name: str) -> bool:
        """
        Whether `name` is referenced inside a `__main__` guard.
        """

        for block in cls._main_blocks(tree):
            for node in ast.walk(block):
                if isinstance(node, ast.Name) and node.id == name:
                    return True

        return False

    @classmethod
    def _used_at_runtime(cls, tree: ast.AST, name: str) -> bool:
        """
        Whether `name` appears anywhere other than an annotation.

        References inside `if __name__ == "__main__":` do not count: that
        block does not execute when the module is imported, so it cannot
        participate in an import cycle.
        """

        main_nodes: set[int] = set()

        for block in cls._main_blocks(tree):
            for inner in ast.walk(block):
                main_nodes.add(id(inner))

        annotation_nodes: set[int] = set()

        for node in ast.walk(tree):
            annotations: list[ast.AST | None] = []

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                annotations.append(node.returns)
                for arg in [
                    *node.args.args,
                    *node.args.posonlyargs,
                    *node.args.kwonlyargs,
                    node.args.vararg,
                    node.args.kwarg,
                ]:
                    if arg is not None:
                        annotations.append(arg.annotation)
            elif isinstance(node, ast.AnnAssign):
                annotations.append(node.annotation)

            for annotation in annotations:
                if annotation is None:
                    continue
                for inner in ast.walk(annotation):
                    annotation_nodes.add(id(inner))

        for node in ast.walk(tree):
            if id(node) in main_nodes:
                continue
            if isinstance(node, ast.Name) and node.id == name:
                if id(node) not in annotation_nodes:
                    return True
            elif isinstance(node, ast.Attribute):
                root: ast.AST = node
                while isinstance(root, ast.Attribute):
                    root = root.value
                if (
                    isinstance(root, ast.Name)
                    and root.id == name
                    and id(node) not in annotation_nodes
                ):
                    return True

        return False

    @staticmethod
    def _annotations_import_index(lines: list[str]) -> int:
        """
        Index just after the last module-level import.

        Only column-zero imports count. Indented ones live inside functions
        or `__main__` guards, and inserting a TYPE_CHECKING block after one
        of those would nest it inside that body.
        """

        last = 0

        for index, line in enumerate(lines):
            if not line or line[0].isspace():
                continue
            if line.startswith(("import ", "from ")):
                last = index + 1

        return last

    @staticmethod
    def _ensure_prelude(source: str) -> str:
        """
        Guarantee `from __future__ import annotations` and the TYPE_CHECKING
        import are present.
        """

        lines = source.splitlines()

        if "from __future__ import annotations" not in source:
            insert_at = 0

            # Keep the module docstring first.
            try:
                tree = ast.parse(source)
                if (
                    tree.body
                    and isinstance(tree.body[0], ast.Expr)
                    and isinstance(tree.body[0].value, ast.Constant)
                    and isinstance(tree.body[0].value.value, str)
                ):
                    insert_at = tree.body[0].end_lineno or 0
            except SyntaxError:
                insert_at = 0

            lines[insert_at:insert_at] = [
                "",
                "from __future__ import annotations",
            ]

        source = "\n".join(lines)

        if "TYPE_CHECKING" not in source.split("if TYPE_CHECKING:")[0]:
            lines = source.splitlines()

            anchor = 0
            for index, line in enumerate(lines):
                if line.strip() == "from __future__ import annotations":
                    anchor = index + 1
                    break

            lines[anchor:anchor] = [
                "",
                "from typing import TYPE_CHECKING",
            ]

            source = "\n".join(lines)

        return source
