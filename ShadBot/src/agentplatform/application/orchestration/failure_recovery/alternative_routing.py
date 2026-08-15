"""
ShadBot Agent Platform

Alternative Agent Routing component for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from agentplatform.domain.agents import AgentRole
from .recovery_strategy import RecoveryStrategy


@dataclass(frozen=True, slots=True)
class AlternativeRoute:
    has_alternative: bool
    alternative_role: AgentRole | None


class AlternativeRouter:
    """
    Reroutes failed execution to an alternative backup agent role.
    """

    def reroute(self, strategy: RecoveryStrategy) -> AlternativeRoute:
        if strategy.reroute_role == "architect":
            return AlternativeRoute(True, AgentRole.ARCHITECT)
        return AlternativeRoute(False, None)
