"""
ShadBot Agent Platform

Agent profile model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.capabilities import Capability


@dataclass(frozen=True, slots=True)
class AgentProfile:
    """
    Complete definition of an agent.
    """

    role: AgentRole

    description: str

    capabilities: list[Capability] = field(
        default_factory=list,
    )
