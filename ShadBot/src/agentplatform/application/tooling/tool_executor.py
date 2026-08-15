"""
ShadBot Agent Platform

Tool executor.
"""

from __future__ import annotations

from agentplatform.application.tooling.tool_registry import (
    ToolRegistry,
)
from agentplatform.domain.tools import ToolType


class ToolExecutor:
    """
    Executes registered agent tools.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:
        self._registry = registry

    def execute(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> dict[str, object]:
        """
        Execute selected tool.
        """

        if not self._registry.exists(tool_type):
            raise ValueError(
                f"Tool not registered: {tool_type}",
            )

        tool = self._registry.get(
            tool_type,
        )

        return tool.execute(
            payload,
        )
