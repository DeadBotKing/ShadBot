"""
ShadBot Agent Platform

Event Processing Monitor component for 8.1 Event Bus.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventBusMetrics:
    published_count: int
    delivered_count: int
    failed_count: int


class EventProcessingMonitor:
    """
    Monitors event bus delivery metrics and error counts.
    """

    def __init__(self) -> None:
        self._published = 0
        self._delivered = 0
        self._failed = 0

    def record_publish(self, count: int = 1) -> None:
        self._published += count

    def record_delivery(self, count: int = 1) -> None:
        self._delivered += count

    def record_failure(self, count: int = 1) -> None:
        self._failed += count

    def get_metrics(self) -> EventBusMetrics:
        return EventBusMetrics(self._published, self._delivered, self._failed)
