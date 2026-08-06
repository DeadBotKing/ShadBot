"""
ShadBot Agent Platform

Execution monitor adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .execution_monitor import ExecutionMonitor


class ExecutionMonitorAdapter(ToolContract):
    """
    Adapter exposing execution monitoring.
    """

    def __init__(self) -> None:
        self._monitor = ExecutionMonitor()

    @property
    def tool_type(
        self,
    ) -> ToolType:
        return ToolType.EXECUTION_MONITOR

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        action = str(
            payload.get(
                "action",
                "snapshot",
            ),
        )

        if action == "active":
            return {
                "executions": self._monitor.get_active_executions(),
            }

        if action == "history":
            return {
                "executions": self._monitor.get_execution_history(),
            }

        if action == "failed":
            return {
                "executions": self._monitor.get_failed_executions(),
            }

        return self._monitor.snapshot()
