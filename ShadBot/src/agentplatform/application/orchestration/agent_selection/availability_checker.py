"""
ShadBot Agent Platform

Availability Checker component for 6.2 Agent Selection.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.contracts import AgentContract


class AvailabilityChecker:
    """
    Checks operational availability of candidate agents.
    """

    def check_available(self, agents: Sequence[AgentContract]) -> tuple[AgentContract, ...]:
        # Currently all registered agents are stateless and available
        return tuple(agents)
