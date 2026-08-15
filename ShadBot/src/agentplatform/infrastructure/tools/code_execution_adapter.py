"""
ShadBot Agent Platform

Code execution tool adapter.
"""

from __future__ import annotations

import subprocess

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class CodeExecutionAdapter(ToolContract):
    """
    Execute code commands.
    """

    @property
    def tool_type(self) -> ToolType:
        return ToolType.CODE_EXECUTION

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        command = str(
            payload.get("command", ""),
        )

        if not command:
            raise ValueError(
                "Execution command is required.",
            )

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }
