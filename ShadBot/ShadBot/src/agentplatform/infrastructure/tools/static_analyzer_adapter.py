"""
ShadBot Agent Platform

Static analyzer tool adapter.
"""

from __future__ import annotations

import subprocess

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class StaticAnalyzerAdapter(ToolContract):
    """
    Run static analysis tools.
    """

    @property
    def tool_type(self) -> ToolType:
        return ToolType.STATIC_ANALYZER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        path = str(
            payload.get("path", "."),
        )

        command = f"ruff check {path}"

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "errors": result.stderr,
        }
