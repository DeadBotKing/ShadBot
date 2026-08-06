"""
ShadBot Agent Platform

File Reader Tool
"""

from __future__ import annotations

from pathlib import Path


class FileReader:
    """
    Reads file content from workspace.
    """

    def read(
        self,
        path: str,
        encoding: str = "utf-8",
    ) -> str:
        """
        Read file content.
        """

        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if not file_path.is_file():
            raise ValueError(f"Path is not file: {path}")

        return file_path.read_text(
            encoding=encoding,
        )
