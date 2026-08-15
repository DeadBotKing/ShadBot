"""
ShadBot Agent Platform

Agent capability assignment.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.capabilities.capability import (
    Capability,
)


@dataclass(frozen=True, slots=True)
class AgentCapability:
    """
    Maps a capability to an agent role.
    """

    agent_role: AgentRole

    capability: Capability
