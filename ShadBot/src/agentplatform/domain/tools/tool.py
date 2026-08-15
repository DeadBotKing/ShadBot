"""
ShadBot Agent Platform

Tool Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from agentplatform.domain.agents import (
    AgentCapability,
)


@dataclass(frozen=True, slots=True)
class Tool:
    """
    Domain representation of executable agent tool.
    """

    name: str

    description: str

    capability: AgentCapability

    version: str

    tool_id: UUID = field(
        default_factory=uuid4,
    )

    enabled: bool = True

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    def can_execute(
        self,
    ) -> bool:
        """
        Check tool availability.
        """

        return self.enabled
