"""
ShadBot Agent Platform

Event Router component for 8.1 Event Bus.
"""

from __future__ import annotations

from typing import Sequence
from .event_contract import EventListenerContract
from .event_entity import SystemEvent
from .event_subscriber import EventSubscriber


class EventRouter:
    """
    Routes events to matching subscribers.
    """

    def __init__(self, subscriber: EventSubscriber) -> None:
        self._subscriber = subscriber

    def route_event(self, event: SystemEvent) -> int:
        listeners = self._subscriber.get_subscribers(event.event_type)
        delivered = 0
        for listener in listeners:
            try:
                listener.on_event(event)
                delivered += 1
            except Exception:
                continue
        return delivered
