"""
ShadBot Agent Platform

Agent Capability Definition
"""

from __future__ import annotations

from dataclasses import dataclass

from .agent_capability import AgentCapability
from .capability_description import (
    CapabilityDescription,
)
from .capability_requirements import (
    CapabilityRequirements,
)


@dataclass(frozen=True, slots=True)
class CapabilityDefinition:
    """
    Enterprise metadata definition for an agent capability.
    """

    capability: AgentCapability

    description: CapabilityDescription

    requirements: CapabilityRequirements

    name: str

    category: str

    is_autonomous: bool = False

    is_enabled: bool = True
