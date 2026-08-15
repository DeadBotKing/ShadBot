"""
ShadBot Agent Platform

Agent cognitive profile.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from agentplatform.domain.agents import AgentRole

from .profile_capability import ProfileCapability


@dataclass(frozen=True, slots=True)
class AgentProfile:
    """
    Defines complete cognitive identity of an agent.
    """

    role: AgentRole

    name: str

    reasoning_style: str

    planning_style: str

    decision_style: str

    reflection_style: str

    validation_style: str

    capabilities: tuple[ProfileCapability, ...]

    profile_id: UUID = field(
        default_factory=uuid4,
    )
