"""
ShadBot Agent Platform

Agent registry implementation.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.contracts import AgentContract

from .registry_entry import RegistryEntry


class AgentRegistry:
    """
    Central registry for available agents.
    """

    def __init__(self) -> None:
        self._agents: dict[AgentRole, RegistryEntry] = {}

    def register(
        self,
        role: AgentRole,
        agent: AgentContract,
    ) -> None:
        """
        Register an agent.
        """

        self._agents[role] = RegistryEntry(
            role=role,
            agent=agent,
        )

    def get(
        self,
        role: AgentRole,
    ) -> AgentContract:
        """
        Retrieve registered agent.
        """

        entry = self._agents.get(role)

        if entry is None:
            raise KeyError(f"Agent not registered: {role.value}")

        return entry.agent

    def exists(
        self,
        role: AgentRole,
    ) -> bool:
        """
        Check agent availability.
        """

        return role in self._agents

    def count(self) -> int:
        """
        Number of registered agents.
        """

        return len(self._agents)
