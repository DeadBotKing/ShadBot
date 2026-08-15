"""
ShadBot Agent Platform

Tool Permission Control
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


@dataclass(frozen=True, slots=True)
class ToolPermission:
    """
    Defines permission for an agent role
    to execute a tool capability.
    """

    role: AgentRole

    capability: AgentCapability

    allowed: bool = True

    reason: str | None = None

    def can_execute(
        self,
    ) -> bool:
        """
        Check permission state.
        """

        return self.allowed
