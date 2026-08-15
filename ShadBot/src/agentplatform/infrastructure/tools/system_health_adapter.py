"""
ShadBot Agent Platform

System health adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .system_health import SystemHealth


class SystemHealthAdapter(ToolContract):
    """
    Adapter exposing system health checks.
    """

    def __init__(self) -> None:
        self._health = SystemHealth()

    @property
    def tool_type(
        self,
    ) -> ToolType:
        return ToolType.SYSTEM_HEALTH

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

        if action == "platform":
            return self._health.check_platform_health()

        if action == "dependencies":
            return self._health.check_dependencies()

        return self._health.snapshot()
