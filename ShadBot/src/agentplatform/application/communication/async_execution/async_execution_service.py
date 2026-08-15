"""
ShadBot Agent Platform

Unified service for 8.4 Async Execution.
"""

from __future__ import annotations

from typing import Any, Callable
from uuid import UUID, uuid4
from .async_task_model import AsyncTaskModel
from .background_worker import BackgroundTaskWorker
from .progress_tracker import AsyncTaskProgressTracker


class AsyncExecutionService:
    """
    Orchestrates async task creation, background execution, progress tracking, and result notification.
    """

    def __init__(
        self,
        worker: BackgroundTaskWorker | None = None,
        tracker: AsyncTaskProgressTracker | None = None,
    ) -> None:
        self.worker = worker or BackgroundTaskWorker()
        self.tracker = tracker or AsyncTaskProgressTracker()

    def submit_task(
        self,
        name: str,
        payload: dict[str, Any],
        handler: Callable[[dict[str, Any]], Any],
        priority: str = "NORMAL",
    ) -> AsyncTaskModel:
        task = AsyncTaskModel(
            task_id=uuid4(),
            name=name,
            status="QUEUED",
            priority=priority,
            payload=payload,
        )
        self.tracker.track(task)
        completed = self.worker.execute_task(task, handler)
        self.tracker.track(completed)
        return completed
