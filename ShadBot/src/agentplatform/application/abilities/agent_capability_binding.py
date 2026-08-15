"""
ShadBot Agent Platform

Agent Capability Binding
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


@dataclass(slots=True)
class AgentCapabilityBinding:
    """
    Runtime binding between agent role and capabilities.
    """

    agent_role: AgentRole

    capabilities: set[AgentCapability] = field(
        default_factory=set,
    )

    def bind(
        self,
        capability: AgentCapability,
    ) -> None:
        """
        Attach capability to agent.
        """

        self.capabilities.add(
            capability,
        )

    def unbind(
        self,
        capability: AgentCapability,
    ) -> None:
        """
        Remove capability from agent.
        """

        self.capabilities.discard(
            capability,
        )

    def has(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check capability availability.
        """

        return capability in self.capabilities

    def list(
        self,
    ) -> frozenset[AgentCapability]:
        """
        Return immutable capability snapshot.
        """

        return frozenset(
            self.capabilities,
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all runtime capabilities.
        """

        self.capabilities.clear()

    def validate(
        self,
        required: set[AgentCapability],
    ) -> bool:
        """
        Validate capability requirements.
        """

        return required.issubset(
            self.capabilities,
        )
