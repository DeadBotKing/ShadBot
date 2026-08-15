"""
ShadBot Agent Platform

Git tool implementation.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


class GitTool:
    """
    Handles git operations.
    """

    def status(
        self,
        path: str,
    ) -> str:
        return self._execute(
            path,
            "status",
            "--short",
        )

    def diff(
        self,
        path: str,
    ) -> str:
        return self._execute(
            path,
            "diff",
        )

    def log(
        self,
        path: str,
    ) -> str:
        return self._execute(
            path,
            "log",
            "--oneline",
            "-10",
        )

    def _execute(
        self,
        path: str,
        *args: str,
    ) -> str:
        result = subprocess.run(
            [
                "git",
                *args,
            ],
            cwd=Path(path),
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            raise RuntimeError(
                result.stderr.strip(),
            )

        return result.stdout.strip()
