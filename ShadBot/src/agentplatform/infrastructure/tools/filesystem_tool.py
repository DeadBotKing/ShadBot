"""
ShadBot Agent Platform

Filesystem tool.
"""

from __future__ import annotations

from pathlib import Path


class FileSystemTool:
    """
    Handles file operations.
    """

    def write_file(
        self,
        path: str,
        content: str,
    ) -> None:
        """
        Write content to file.
        """

        file_path = Path(path)

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            content,
            encoding="utf-8",
        )

    def read_file(
        self,
        path: str,
    ) -> str:
        """
        Read file content.
        """

        return Path(path).read_text(
            encoding="utf-8",
        )
