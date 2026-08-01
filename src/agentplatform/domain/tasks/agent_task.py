"""
ShadBot Agent Platform

Agent task domain model.
"""

from __future__ import annotations

from dataclasses import dataclass
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

    id: UUID = uuid4()

    status: TaskStatus = TaskStatus.CREATED

    created_at: datetime = datetime.now(timezone.utc)

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
