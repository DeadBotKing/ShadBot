"""
ShadBot Agent Platform

File Writer Tool
"""

from __future__ import annotations

from pathlib import Path


class FileWriter:
    """
    Writes content into existing files.
    """

    def write(
        self,
        path: str,
        content: str,
        encoding: str = "utf-8",
    ) -> None:
        """
        Write file content.
        """

        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        file_path.write_text(
            content,
            encoding=encoding,
        )
