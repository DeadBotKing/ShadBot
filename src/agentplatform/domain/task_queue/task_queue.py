"""
ShadBot Agent Platform

Task queue.
"""

from __future__ import annotations

from collections import deque

from agentplatform.domain.task_queue.queued_task import QueuedTask


class TaskQueue:
    """
    FIFO task queue.
    """

    def __init__(self) -> None:
        self._queue: deque[QueuedTask] = deque()

    def enqueue(
        self,
        queued_task: QueuedTask,
    ) -> None:
        self._queue.append(
            queued_task,
        )

    def dequeue(
        self,
    ) -> QueuedTask | None:
        if not self._queue:
            return None

        return self._queue.popleft()

    def is_empty(
        self,
    ) -> bool:
        return not self._queue

    def size(
        self,
    ) -> int:
        return len(
            self._queue,
        )
