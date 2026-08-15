"""
ShadBot Agent Platform

Directory Creator Tool
"""

from pathlib import Path


class DirectoryCreator:
    """
    Creates directories.
    """

    def create(
        self,
        path: str,
    ) -> None:
        """
        Create directory tree.
        """

        Path(path).mkdir(
            parents=True,
            exist_ok=True,
        )
