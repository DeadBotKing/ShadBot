"""
Agent Platform

Agent Definition Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet

from agentplatform.domain.agents.agent_capability import AgentCapability
from agentplatform.domain.agents.agent_role import AgentRole


@dataclass(frozen=True)
class AgentDefinition:
    """
    Immutable definition of an AI agent.
    """

    name: str

    role: AgentRole

    capabilities: FrozenSet[AgentCapability]

    preferred_model: str

    fallback_model: str | None = None
