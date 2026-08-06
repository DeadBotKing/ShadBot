"""
ShadBot Agent Platform

Experiment executor tool adapter.
"""

from __future__ import annotations

import subprocess

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class ExperimentExecutorAdapter(ToolContract):
    """
    Execute research experiments.
    """

    @property
    def tool_type(self) -> ToolType:
        return ToolType.EXPERIMENT_EXECUTOR

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        command = str(
            payload.get("command", ""),
        )

        if not command:
            raise ValueError(
                "Experiment command required.",
            )

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
