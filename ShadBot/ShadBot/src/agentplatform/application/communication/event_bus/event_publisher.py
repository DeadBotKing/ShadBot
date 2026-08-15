"""
ShadBot Agent Platform

Unified Event Publisher service for 8.1 Event Bus.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4
from .event_entity import SystemEvent
from .event_monitor import EventProcessingMonitor
from .event_persistence import EventPersistence
from .event_queue import EventQueueManager
from .event_router import EventRouter
from .event_subscriber import EventSubscriber


class EventBusService:
    """
    Orchestrates event publishing, queueing, routing, persistence, and monitoring.
    """

    def __init__(
        self,
        subscriber: EventSubscriber | None = None,
        router: EventRouter | None = None,
        queue: EventQueueManager | None = None,
        persistence: EventPersistence | None = None,
        monitor: EventProcessingMonitor | None = None,
    ) -> None:
        self.subscriber = subscriber or EventSubscriber()
        self.router = router or EventRouter(self.subscriber)
        self.queue = queue or EventQueueManager()
        self.persistence = persistence or EventPersistence()
        self.monitor = monitor or EventProcessingMonitor()

    def publish(
        self,
        event_type: str,
        source: str,
        payload: dict[str, Any],
        correlation_id: UUID | None = None,
    ) -> SystemEvent:
        event = SystemEvent(
            event_id=uuid4(),
            event_type=event_type,
            source_component=source,
            payload=payload,
            correlation_id=correlation_id or uuid4(),
        )
        self.persistence.save_event(event)
        self.monitor.record_publish()
        delivered = self.router.route_event(event)
        self.monitor.record_delivery(delivered)
        return event
