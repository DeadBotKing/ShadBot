"""
ShadBot Agent Platform

Action Request Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


@dataclass(frozen=True, slots=True)
class ActionRequest:
    """
    Represents an agent request to execute an action.
    """

    agent_role: AgentRole

    capability: AgentCapability

    payload: dict[str, object]

    request_id: UUID = field(
        default_factory=uuid4,
    )

    project_id: UUID | None = None

    priority: int = 0

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    def with_priority(
        self,
        priority: int,
    ) -> "ActionRequest":
        """
        Create request with updated priority.
        """

        return ActionRequest(
            agent_role=self.agent_role,
            capability=self.capability,
            payload=self.payload,
            request_id=self.request_id,
            project_id=self.project_id,
            priority=priority,
            metadata=self.metadata,
            created_at=self.created_at,
        )

    def with_metadata(
        self,
        metadata: dict[str, object],
    ) -> "ActionRequest":
        """
        Create request with additional metadata.
        """

        merged_metadata = {
            **self.metadata,
            **metadata,
        }

        return ActionRequest(
            agent_role=self.agent_role,
            capability=self.capability,
            payload=self.payload,
            request_id=self.request_id,
            project_id=self.project_id,
            priority=self.priority,
            metadata=merged_metadata,
            created_at=self.created_at,
        )
