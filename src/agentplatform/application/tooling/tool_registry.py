"""
ShadBot Agent Platform

Tool registry.
"""

from __future__ import annotations

from agentplatform.domain.tooling import ToolDefinition
from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class ToolRegistry:
    """
    Stores available agent tools.
    """

    def __init__(self) -> None:
        self._definitions: dict[
            ToolType,
            ToolDefinition,
        ] = {}

        self._implementations: dict[
            ToolType,
            ToolContract,
        ] = {}

    def register(
        self,
        tool: ToolDefinition,
        implementation: ToolContract,
    ) -> None:
        self._definitions[tool.tool_type] = tool
        self._implementations[tool.tool_type] = implementation

    def exists(
        self,
        tool_type: ToolType,
    ) -> bool:
        return tool_type in self._implementations

    def get(
        self,
        tool_type: ToolType,
    ) -> ToolContract:
        return self._implementations[tool_type]

    def get_definition(
        self,
        tool_type: ToolType,
    ) -> ToolDefinition:
        return self._definitions[tool_type]

    def count(self) -> int:
        return len(self._implementations)
