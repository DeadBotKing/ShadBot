"""
ShadBot Agent Platform

Event Subscriber component for 8.1 Event Bus.
"""

from __future__ import annotations

from collections import defaultdict
from .event_contract import EventListenerContract
from .event_entity import SystemEvent


class EventSubscriber:
    """
    Manages event listener registrations and subscriber lookup.
    """

    def __init__(self) -> None:
        self._listeners: dict[str, list[EventListenerContract]] = defaultdict(list)
        self._global_listeners: list[EventListenerContract] = []

    def subscribe(self, event_type: str, listener: EventListenerContract) -> None:
        self._listeners[event_type].append(listener)

    def subscribe_all(self, listener: EventListenerContract) -> None:
        self._global_listeners.append(listener)

    def get_subscribers(self, event_type: str) -> tuple[EventListenerContract, ...]:
        specific = self._listeners.get(event_type, [])
        return tuple(specific + self._global_listeners)
