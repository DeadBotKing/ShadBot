"""
ShadBot Agent Platform

Metrics collector adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .metrics_collector import MetricsCollector


class MetricsCollectorAdapter(ToolContract):
    """
    Adapter exposing metrics collection.
    """

    def __init__(self) -> None:
        self._collector = MetricsCollector()

    @property
    def tool_type(
        self,
    ) -> ToolType:
        return ToolType.METRICS_COLLECTOR

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

        if action == "execution":
            return self._collector.collect_execution_metrics()

        if action == "agents":
            return self._collector.collect_agent_metrics()

        if action == "system":
            return self._collector.collect_system_metrics()

        return self._collector.snapshot()
