"""
ShadBot Agent Platform

Event Persistence component for 8.1 Event Bus.
"""

from __future__ import annotations

from uuid import UUID
from .event_entity import SystemEvent


class EventPersistence:
    """
    Stores historical system events for audit and recovery.
    """

    def __init__(self) -> None:
        self._stored: dict[UUID, SystemEvent] = {}

    def save_event(self, event: SystemEvent) -> SystemEvent:
        self._stored[event.event_id] = event
        return event

    def get_event(self, event_id: UUID) -> SystemEvent | None:
        return self._stored.get(event_id)

    def get_all(self) -> tuple[SystemEvent, ...]:
        return tuple(self._stored.values())
