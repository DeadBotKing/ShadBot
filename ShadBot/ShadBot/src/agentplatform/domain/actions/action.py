"""
ShadBot Agent Platform

Action Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


class ActionStatus(str, Enum):
    """
    Action lifecycle states.
    """

    CREATED = "created"

    QUEUED = "queued"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"


@dataclass(frozen=True, slots=True)
class Action:
    """
    Domain entity representing an agent action request.
    """

    agent_role: AgentRole

    capability: AgentCapability

    input_payload: dict[str, object]

    action_id: UUID = field(
        default_factory=uuid4,
    )

    status: ActionStatus = ActionStatus.CREATED

    execution_id: UUID | None = None

    output: object | None = None

    error: str | None = None

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    def start(
        self,
        execution_id: UUID,
    ) -> "Action":
        """
        Mark action as running.
        """

        return Action(
            agent_role=self.agent_role,
            capability=self.capability,
            input_payload=self.input_payload,
            action_id=self.action_id,
            status=ActionStatus.RUNNING,
            execution_id=execution_id,
            output=self.output,
            error=self.error,
            created_at=self.created_at,
            updated_at=datetime.now(
                timezone.utc,
            ),
        )

    def complete(
        self,
        output: object,
    ) -> "Action":
        """
        Mark action as completed.
        """

        return Action(
            agent_role=self.agent_role,
            capability=self.capability,
            input_payload=self.input_payload,
            action_id=self.action_id,
            status=ActionStatus.COMPLETED,
            execution_id=self.execution_id,
            output=output,
            error=None,
            created_at=self.created_at,
            updated_at=datetime.now(
                timezone.utc,
            ),
        )

    def fail(
        self,
        error: str,
    ) -> "Action":
        """
        Mark action as failed.
        """

        return Action(
            agent_role=self.agent_role,
            capability=self.capability,
            input_payload=self.input_payload,
            action_id=self.action_id,
            status=ActionStatus.FAILED,
            execution_id=self.execution_id,
            output=None,
            error=error,
            created_at=self.created_at,
            updated_at=datetime.now(
                timezone.utc,
            ),
        )
