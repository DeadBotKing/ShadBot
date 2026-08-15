"""
ShadBot Agent Platform

Capability Tool Binding
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import (
    AgentCapability,
)
from agentplatform.domain.tools import (
    ToolType,
)


@dataclass(slots=True)
class CapabilityToolBinding:
    """
    Runtime binding between capabilities and tools.
    """

    mappings: dict[
        AgentCapability,
        set[ToolType],
    ] = field(
        default_factory=dict,
    )

    def bind(
        self,
        capability: AgentCapability,
        tool_type: ToolType,
    ) -> None:
        """
        Attach tool to capability.
        """

        if capability not in self.mappings:
            self.mappings[capability] = set()

        self.mappings[capability].add(
            tool_type,
        )

    def unbind(
        self,
        capability: AgentCapability,
        tool_type: ToolType,
    ) -> None:
        """
        Remove tool mapping.
        """

        tools = self.mappings.get(
            capability,
        )

        if tools is None:
            return

        tools.discard(
            tool_type,
        )

        if not tools:
            self.mappings.pop(
                capability,
                None,
            )

    def resolve(
        self,
        capability: AgentCapability,
    ) -> frozenset[ToolType]:
        """
        Resolve tools assigned to capability.
        """

        return frozenset(
            self.mappings.get(
                capability,
                set(),
            ),
        )

    def can_use(
        self,
        capability: AgentCapability,
        tool_type: ToolType,
    ) -> bool:
        """
        Validate capability tool access.
        """

        return tool_type in self.mappings.get(
            capability,
            set(),
        )

    def replace(
        self,
        capability: AgentCapability,
        tools: set[ToolType],
    ) -> None:
        """
        Replace capability tool mappings.
        """

        self.mappings[capability] = set(
            tools,
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all mappings.
        """

        self.mappings.clear()
