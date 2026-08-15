"""
ShadBot Agent Platform

Event Queue Management component for 8.1 Event Bus.
"""

from __future__ import annotations

from collections import deque
from .event_entity import SystemEvent


class EventQueueManager:
    """
    Manages queued system events waiting for processing.
    """

    def __init__(self) -> None:
        self._queue: deque[SystemEvent] = deque()

    def enqueue(self, event: SystemEvent) -> None:
        self._queue.append(event)

    def dequeue(self) -> SystemEvent | None:
        if not self._queue:
            return None
        return self._queue.popleft()

    def count(self) -> int:
        return len(self._queue)
