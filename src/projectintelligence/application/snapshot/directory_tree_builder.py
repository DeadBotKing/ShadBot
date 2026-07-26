"""
ShadBot Project Intelligence

Directory Tree Builder
"""

from __future__ import annotations

from pathlib import Path


class DirectoryTreeBuilder:
    """
    Builds a hierarchical directory tree from project files.
    """

    def build(
        self,
        files: list[Path],
        workspace: Path,
    ) -> dict[str, object]:
        """
        Build a directory tree using workspace-relative paths.
        """

        tree: dict[str, object] = {}

        for file_path in files:
            relative_parts = file_path.relative_to(workspace).parts

            current = tree

            for part in relative_parts:
                current = current.setdefault(part, {})

        return tree
