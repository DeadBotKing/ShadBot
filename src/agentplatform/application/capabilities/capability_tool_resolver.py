"""
ShadBot Agent Platform

Capability Tool Resolver
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.tools import (
    ToolRegistry,
)
from agentplatform.domain.agents import (
    AgentCapability,
)
from agentplatform.domain.tools import (
    Tool,
)


@dataclass(slots=True)
class CapabilityToolResolver:
    """
    Resolves tools available for a capability.

    Responsibilities:
    - Capability based lookup.
    - Tool availability filtering.
    - Runtime tool selection.
    """

    registry: ToolRegistry

    def resolve(
        self,
        capability: AgentCapability,
    ) -> list[Tool]:
        """
        Resolve tools mapped to capability.
        """

        resolved: list[Tool] = []

        for tool in self.registry.list():

            if tool.capability != capability:
                continue

            if not tool.can_execute():
                continue

            resolved.append(
                tool,
            )

        resolved.sort(
            key=lambda item: (
                item.name,
                item.version,
            ),
        )

        return resolved

    def resolve_one(
        self,
        capability: AgentCapability,
    ) -> Tool:
        """
        Resolve single executable tool.
        """

        tools = self.resolve(
            capability,
        )

        if not tools:
            raise LookupError(
                ("No enabled tool found " f"for capability '{capability.value}'."),
            )

        return tools[0]

    def supports(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check tool availability.
        """

        return bool(
            self.resolve(
                capability,
            ),
        )
