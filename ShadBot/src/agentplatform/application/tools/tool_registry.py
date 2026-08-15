"""
ShadBot Agent Platform

Tool Registry
"""

from __future__ import annotations

from agentplatform.application.tools.tool_contract import (
    ToolContract,
)
from agentplatform.domain.agents import AgentCapability


class ToolRegistry:
    """
    Central registry for runtime tools.
    """

    def __init__(
        self,
    ) -> None:

        self._tools: dict[
            str,
            ToolContract,
        ] = {}

    def register(
        self,
        tool: ToolContract,
    ) -> None:
        """
        Register executable tool.
        """

        self._tools[tool.definition.name] = tool

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove tool.
        """

        self._tools.pop(
            name,
            None,
        )

    def get(
        self,
        name: str,
    ) -> ToolContract | None:
        """
        Find tool by name.
        """

        return self._tools.get(
            name,
        )

    def has(
        self,
        name: str,
    ) -> bool:
        """
        Check tool existence.
        """

        return name in self._tools

    def find_by_capability(
        self,
        capability: AgentCapability,
    ) -> list[ToolContract]:
        """
        Find tools supporting capability.
        """

        return [
            tool
            for tool in self._tools.values()
            if tool.definition.capability == capability
        ]

    def all(
        self,
    ) -> list[ToolContract]:
        """
        Return all registered tools.
        """

        return list(
            self._tools.values(),
        )

    def count(
        self,
    ) -> int:
        """
        Return registered tool count.
        """

        return len(
            self._tools,
        )
