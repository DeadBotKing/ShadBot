"""
ShadBot Project Intelligence

Ignore Manager
"""

from __future__ import annotations

from pathlib import Path


class IgnoreManager:
    """
    Determines whether a file or directory
    should be ignored during scanning.
    """

    DEFAULT_IGNORES = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        ".pytest_cache",
        ".idea",
        ".vscode",
        "node_modules",
        "dist",
        "build",
        "bin",
        "obj",
        "coverage",
        ".cache",
    }

    def should_ignore(
        self,
        path: Path,
    ) -> bool:
        """
        Returns True if the given path
        should be ignored.
        """

        return any(part in self.DEFAULT_IGNORES for part in path.parts)
