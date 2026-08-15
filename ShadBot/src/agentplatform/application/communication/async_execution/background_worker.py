"""
ShadBot Agent Platform

Background Task Worker component for 8.4 Async Execution.
"""

from __future__ import annotations

from typing import Any, Callable
from .async_task_model import AsyncTaskModel


class BackgroundTaskWorker:
    """
    Executes an async task in a managed execution boundary.
    """

    def execute_task(self, task: AsyncTaskModel, handler: Callable[[dict[str, Any]], Any]) -> AsyncTaskModel:
        try:
            res = handler(task.payload)
            return AsyncTaskModel(
                task_id=task.task_id,
                name=task.name,
                status="COMPLETED",
                priority=task.priority,
                payload=task.payload,
                result=res,
                created_at=task.created_at,
            )
        except Exception as exc:
            return AsyncTaskModel(
                task_id=task.task_id,
                name=task.name,
                status="FAILED",
                priority=task.priority,
                payload=task.payload,
                result={"error": str(exc)},
                created_at=task.created_at,
            )
