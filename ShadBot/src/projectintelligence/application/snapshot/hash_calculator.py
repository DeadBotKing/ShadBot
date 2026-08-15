"""
ShadBot Project Intelligence

Hash Calculator
"""

from __future__ import annotations

import hashlib
from pathlib import Path


class HashCalculator:
    """
    Calculates SHA-256 hashes for project files.
    """

    _BUFFER_SIZE = 1024 * 1024  # 1 MB

    def calculate(
        self,
        file_path: Path,
    ) -> str:
        """
        Calculate the SHA-256 hash of a file.
        """

        sha256 = hashlib.sha256()

        with file_path.open("rb") as file:
            while chunk := file.read(self._BUFFER_SIZE):
                sha256.update(chunk)

        return sha256.hexdigest()

    def calculate_many(
        self,
        files: list[Path],
        workspace: Path,
    ) -> dict[str, str]:
        """
        Calculate hashes for multiple files.

        Keys are stored as workspace-relative paths.
        """

        hashes: dict[str, str] = {}

        for file_path in files:
            relative_path = file_path.relative_to(workspace).as_posix()
            hashes[relative_path] = self.calculate(file_path)

        return hashes
