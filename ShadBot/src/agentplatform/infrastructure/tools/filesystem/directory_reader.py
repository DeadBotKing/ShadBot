"""
ShadBot Agent Platform

Directory Reader Tool
"""

from pathlib import Path


class DirectoryReader:
    """
    Lists directory contents.
    """

    def list(
        self,
        path: str,
    ) -> list[str]:
        """
        Return directory entries.
        """

        directory = Path(path)

        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {path}")

        if not directory.is_dir():
            raise ValueError(f"Path is not directory: {path}")

        return [item.name for item in directory.iterdir()]
