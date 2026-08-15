"""
ShadBot Agent Platform

Event Contract interface for 8.1 Event Bus.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from .event_entity import SystemEvent


class EventListenerContract(ABC):
    """
    Contract for subscribing to and handling system events.
    """

    @abstractmethod
    def on_event(self, event: SystemEvent) -> None:
        raise NotImplementedError
