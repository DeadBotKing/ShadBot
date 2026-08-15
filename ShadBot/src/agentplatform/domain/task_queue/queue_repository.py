"""
ShadBot Agent Platform

Task queue repository contract.
"""

from __future__ import annotations

from typing import Protocol

from agentplatform.domain.task_queue.queued_task import QueuedTask


class QueueRepository(Protocol):
    """
    Queue persistence contract.
    """

    def enqueue(
        self,
        queued_task: QueuedTask,
    ) -> None: ...

    def dequeue(
        self,
    ) -> QueuedTask | None: ...

    def size(
        self,
    ) -> int: ...
