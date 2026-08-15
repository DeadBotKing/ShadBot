"""
ShadBot Agent Platform

Capability registry.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.capabilities import Capability


class CapabilityRegistry:
    """
    Stores capabilities assigned to agents.
    """

    def __init__(self) -> None:
        self._capabilities: dict[
            AgentRole,
            list[Capability],
        ] = {}

    def register(
        self,
        role: AgentRole,
        capability: Capability,
    ) -> None:
        """
        Register capability for agent.
        """

        if role not in self._capabilities:
            self._capabilities[role] = []

        self._capabilities[role].append(capability)

    def get(
        self,
        role: AgentRole,
    ) -> list[Capability]:
        """
        Get capabilities of an agent.
        """

        return self._capabilities.get(role, [])

    def count(
        self,
        role: AgentRole,
    ) -> int:
        """
        Count capabilities of an agent.
        """

        return len(self.get(role))
