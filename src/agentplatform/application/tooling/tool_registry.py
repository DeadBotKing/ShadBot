"""
ShadBot Agent Platform

Tool registry.
"""

from __future__ import annotations

from agentplatform.domain.tooling import ToolDefinition
from agentplatform.domain.tools import ToolType


class ToolRegistry:
    """
    Stores available tools.
    """

    def __init__(self) -> None:
        self._tools: dict[ToolType, ToolDefinition] = {}

    def register(
        self,
        tool: ToolDefinition,
    ) -> None:
        """
        Register tool.
        """

        self._tools[tool.tool_type] = tool

    def exists(
        self,
        tool_type: ToolType,
    ) -> bool:
        """
        Check tool availability.
        """

        return tool_type in self._tools

    def get(
        self,
        tool_type: ToolType,
    ) -> ToolDefinition:
        """
        Retrieve tool definition.
        """

        return self._tools[tool_type]

    def count(self) -> int:
        """
        Number of registered tools.
        """

        return len(self._tools)
