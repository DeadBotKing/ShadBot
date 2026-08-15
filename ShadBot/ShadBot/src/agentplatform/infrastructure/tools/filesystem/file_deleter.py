"""
ShadBot Agent Platform

File Delete Tool
"""

from pathlib import Path


class FileDeleter:
    """
    Deletes files.
    """

    def delete(
        self,
        path: str,
    ) -> None:
        """
        Delete file.
        """

        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        file_path.unlink()
