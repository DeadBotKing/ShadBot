"""
ShadBot Agent Platform

Capability Binding
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import AgentCapability


@dataclass(slots=True)
class CapabilityBinding:
    """
    Runtime capability binding.
    """

    capabilities: set[AgentCapability] = field(
        default_factory=set,
    )

    def has(
        self,
        capability: AgentCapability,
    ) -> bool:
        return capability in self.capabilities

    def add(
        self,
        capability: AgentCapability,
    ) -> None:
        self.capabilities.add(
            capability,
        )

    def remove(
        self,
        capability: AgentCapability,
    ) -> None:
        self.capabilities.discard(
            capability,
        )
