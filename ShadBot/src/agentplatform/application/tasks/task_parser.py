"""
ShadBot Agent Platform

Task parser.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.tasks import (
    AgentTask,
    TaskType,
)


class TaskParser:
    """
    Converts raw task data into domain tasks.
    """

    def parse(
        self,
        data: dict[str, object],
    ) -> AgentTask:
        """
        Parse task definition.
        """

        return AgentTask(
            id=UUID(str(data["id"])),
            title=str(data["title"]),
            description=str(data["description"]),
            task_type=TaskType(
                str(data["task_type"]),
            ),
        )
