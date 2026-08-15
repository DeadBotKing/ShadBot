"""
ShadBot Agent Platform

Task lifecycle management.
"""

from __future__ import annotations

from pathlib import Path
from shutil import move

from agentplatform.domain.tasks import (
    AgentTask,
    TaskStatus,
)


class TaskLifecycleManager:
    """
    Handles task state transitions.
    """

    def mark_running(
        self,
        task: AgentTask,
    ) -> AgentTask:
        """
        Mark task as running.
        """

        return AgentTask(
            id=task.id,
            title=task.title,
            description=task.description,
            task_type=task.task_type,
            status=TaskStatus.RUNNING,
            created_at=task.created_at,
        )

    def mark_completed(
        self,
        task: AgentTask,
    ) -> AgentTask:
        """
        Mark task as completed.
        """

        return task.complete()

    def archive_task(
        self,
        task_file: Path,
        completed_dir: Path,
    ) -> None:
        """
        Move completed task file.
        """

        completed_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        move(
            str(task_file),
            str(completed_dir / task_file.name),
        )
