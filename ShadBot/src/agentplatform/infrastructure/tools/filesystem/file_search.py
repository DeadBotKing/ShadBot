"""
ShadBot Agent Platform

File Search Tool
"""

from pathlib import Path


class FileSearch:
    """
    Searches files in workspace.
    """

    def search(
        self,
        root: str,
        pattern: str,
    ) -> list[str]:

        base = Path(root)

        return [str(file) for file in base.rglob(pattern) if file.is_file()]
