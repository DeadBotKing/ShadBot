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
            check=False,
        )

        if result.returncode != 0:
            raise RuntimeError(
                result.stderr.strip(),
            )

        return result.stdout.strip()
