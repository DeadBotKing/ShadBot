"""
ShadBot Agent Platform

Terminal tool implementation.
"""

from __future__ import annotations

import subprocess


class TerminalTool:
    """
    Handles terminal command execution.
    """

    def execute(
        self,
        command: str,
        path: str,
    ) -> str:
        result = subprocess.run(
            command,
            cwd=path,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

        if result.returncode != 0:
            detail = (
                (result.stderr or "").strip()
                or (result.stdout or "").strip()
                or f"Command failed with exit code {result.returncode}: {command}"
            )
            raise RuntimeError(detail)

        return (result.stdout or "").strip()
