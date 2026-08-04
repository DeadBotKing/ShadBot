"""
ShadBot Agent Platform

Agent task domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from agentplatform.domain.tasks.task_status import TaskStatus
from agentplatform.domain.tasks.task_type import TaskType


@dataclass(frozen=True, slots=True)
class AgentTask:
    """
    Represents a unit of work assigned to an agent.
    """

    title: str

    description: str

    task_type: TaskType

    id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    status: TaskStatus = TaskStatus.CREATED

    def assign(self) -> "AgentTask":
        """
        Mark task as assigned.
        """

        return AgentTask(
            id=self.id,
            title=self.title,
            description=self.description,
            task_type=self.task_type,
            status=TaskStatus.ASSIGNED,
            created_at=self.created_at,
        )

    def complete(self) -> "AgentTask":
        """
        Mark task as completed.
        """

        return AgentTask(
            id=self.id,
            title=self.title,
            description=self.description,
            task_type=self.task_type,
            status=TaskStatus.COMPLETED,
            created_at=self.created_at,
        )
