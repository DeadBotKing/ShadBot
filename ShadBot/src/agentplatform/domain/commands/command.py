"""
ShadBot Agent Platform

Command Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from agentplatform.domain.agents import (
    AgentRole,
)


@dataclass(frozen=True, slots=True)
class Command:
    """
    Represents an executable command
    issued by an agent.
    """

    name: str

    issuer: AgentRole

    payload: dict[str, Any]

    command_id: UUID = field(
        default_factory=uuid4,
    )

    target_agent: AgentRole | None = None

    priority: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    def is_targeted(
        self,
    ) -> bool:
        """
        Check if command targets specific agent.
        """

        return self.target_agent is not None

    def with_priority(
        self,
        priority: int,
    ) -> "Command":
        """
        Create command with new priority.
        """

        return Command(
            name=self.name,
            issuer=self.issuer,
            payload=self.payload,
            command_id=self.command_id,
            target_agent=self.target_agent,
            priority=priority,
            metadata=self.metadata,
            created_at=self.created_at,
        )

    def with_metadata(
        self,
        metadata: dict[str, Any],
    ) -> "Command":
        """
        Create command with merged metadata.
        """

        return Command(
            name=self.name,
            issuer=self.issuer,
            payload=self.payload,
            command_id=self.command_id,
            target_agent=self.target_agent,
            priority=self.priority,
            metadata={
                **self.metadata,
                **metadata,
            },
            created_at=self.created_at,
        )
