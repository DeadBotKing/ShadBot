"""
ShadBot Agent Platform

Task Progress Tracking component for 8.4 Async Execution.
"""

from __future__ import annotations

from uuid import UUID
from .async_task_model import AsyncTaskModel


class AsyncTaskProgressTracker:
    """
    Tracks active and completed async tasks.
    """

    def __init__(self) -> None:
        self._tasks: dict[UUID, AsyncTaskModel] = {}

    def track(self, task: AsyncTaskModel) -> None:
        self._tasks[task.task_id] = task

    def get_task(self, task_id: UUID) -> AsyncTaskModel | None:
        return self._tasks.get(task_id)

    def get_all(self) -> tuple[AsyncTaskModel, ...]:
        return tuple(self._tasks.values())
