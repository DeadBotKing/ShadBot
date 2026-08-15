"""
ShadBot Agent Platform

Agent registry entry model.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.contracts import (
    AgentContract,
)


@dataclass(frozen=True, slots=True)
class RegistryEntry:
    """
    Registered agent metadata.
    """

    role: AgentRole

    agent: AgentContract
