"""
ShadBot Agent Platform

Build runner tool.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


class BuildRunner:
    """
    Executes project build validation.
    """

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        """
        Run build process.
        """

        path = Path(
            str(
                payload.get("path", "."),
            ),
        )

        result = subprocess.run(
            [
                "python",
                "-m",
                "compileall",
                str(path),
            ],
            capture_output=True,
            text=True,
            timeout=600,
        )

        return {
            "success": result.returncode == 0,
            "command": "python -m compileall",
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
