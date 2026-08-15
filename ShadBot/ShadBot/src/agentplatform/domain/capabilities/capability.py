"""
ShadBot Agent Platform

Capability domain model.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.capabilities.capability_type import (
    CapabilityType,
)


@dataclass(frozen=True, slots=True)
class Capability:
    """
    Represents an agent capability.
    """

    capability_type: CapabilityType

    description: str
