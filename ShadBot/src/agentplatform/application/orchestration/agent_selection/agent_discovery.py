"""
ShadBot Agent Platform

Agent Discovery component for 6.2 Agent Selection.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.application.registry import AgentRegistry
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.contracts import AgentContract


class AgentDiscovery:
    """
    Discovers available registered agents matching candidate roles.
    """

    def __init__(self, registry: AgentRegistry) -> None:
        self._registry = registry

    def discover(self, candidate_roles: Sequence[AgentRole]) -> tuple[AgentContract, ...]:
        agents: list[AgentContract] = []
        for role in candidate_roles:
            try:
                agent = self._registry.get(role)
                agents.append(agent)
            except Exception:
                continue
        return tuple(agents)
