"""
ShadBot Agent Platform

Agent dispatcher.
"""

from __future__ import annotations

from agentplatform.application.registry import (
    AgentRegistry,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.contracts import (
    AgentContract,
)


class AgentDispatcher:
    """
    Dispatches execution to registered agents.
    """

    def __init__(
        self,
        registry: AgentRegistry,
    ) -> None:
        self._registry = registry

    def dispatch(
        self,
        role: AgentRole,
    ) -> AgentContract:
        """
        Resolve agent by role.
        """

        if not self._registry.exists(
            role,
        ):
            raise KeyError(
                f"Agent not available: {role.value}",
            )

        return self._registry.get(
            role,
        )
