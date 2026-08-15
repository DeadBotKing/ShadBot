"""
ShadBot Agent Platform

File Creator Tool
"""

from __future__ import annotations

from pathlib import Path


class FileCreator:
    """
    Creates new files.
    """

    def create(
        self,
        path: str,
        content: str = "",
        encoding: str = "utf-8",
    ) -> None:
        """
        Create file.
        """

        file_path = Path(path)

        if file_path.exists():
            raise FileExistsError(f"File already exists: {path}")

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            content,
            encoding=encoding,
        )
