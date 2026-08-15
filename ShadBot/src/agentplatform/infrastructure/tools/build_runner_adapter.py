"""
ShadBot Agent Platform

Build runner adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .build_runner import BuildRunner


class BuildRunnerAdapter(ToolContract):
    """
    Adapter exposing build execution as agent tool.
    """

    def __init__(self) -> None:
        self._runner = BuildRunner()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.BUILD_RUNNER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        return self._runner.execute(
            payload,
        )
