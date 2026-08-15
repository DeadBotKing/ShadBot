"""
ShadBot Agent Platform

Task execution context builder.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.tasks import (
    AgentTask,
)
from agentplatform.domain.workspace import (
    Project,
    Workspace,
)


class TaskExecutionBuilder:
    """
    Builds agent execution context from selected tasks.
    """

    def build(
        self,
        task: AgentTask,
        workspace: Workspace,
        project: Project,
    ) -> AgentExecutionContext:
        """
        Create execution context for agents.
        """

        return AgentExecutionContext(
            project_id=uuid4(),
            task_id=task.id,
            instructions=(f"Execute task: {task.title}"),
            workspace=workspace,
            target_project=project,
            task_title=task.title,
            task_description=task.description,
            task_type=task.task_type.value,
            metadata={
                "task": {
                    "title": task.title,
                    "description": task.description,
                    "type": task.task_type.value,
                },
            },
        )
