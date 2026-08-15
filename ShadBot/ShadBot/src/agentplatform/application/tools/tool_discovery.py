"""
ShadBot Agent Platform

Tool Discovery Service
"""

from __future__ import annotations

from agentplatform.application.tools.tool_contract import (
    ToolContract,
)
from agentplatform.application.tools.tool_registry import (
    ToolRegistry,
)
from agentplatform.domain.agents import (
    AgentCapability,
)


class ToolDiscovery:
    """
    Discovers available tools for agents.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:

        self._registry = registry

    def discover_all(
        self,
    ) -> list[ToolContract]:
        """
        Return all available tools.
        """

        return [tool for tool in self._registry.all() if tool.is_available()]

    def discover_by_capability(
        self,
        capability: AgentCapability,
    ) -> list[ToolContract]:
        """
        Find available tools by capability.
        """

        return [
            tool
            for tool in self._registry.find_by_capability(
                capability,
            )
            if tool.is_available()
        ]

    def discover_by_category(
        self,
        category: str,
    ) -> list[ToolContract]:
        """
        Find available tools by metadata category.
        """

        return [
            tool
            for tool in self.discover_all()
            if tool.definition.metadata.get(
                "category",
            )
            == category
        ]

    def exists_for_capability(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check if usable tool exists.
        """

        return bool(
            self.discover_by_capability(
                capability,
            )
        )
