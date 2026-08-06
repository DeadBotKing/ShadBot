"""
ShadBot Agent Platform

Capability Permission Model
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


@dataclass(frozen=True, slots=True)
class CapabilityPermission:
    """
    Defines execution permission for a capability.
    """

    role: AgentRole

    capability: AgentCapability

    allowed: bool = True

    reason: str | None = None

    def can_execute(
        self,
    ) -> bool:
        """
        Check execution permission.
        """

        return self.allowed
