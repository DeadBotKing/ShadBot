"""
ShadBot Agent Platform

Unit tests for 8.1 Event Bus.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.communication.event_bus import (
    EventBusService,
    EventListenerContract,
    EventProcessingMonitor,
    SystemEvent,
)


class FakeListener(EventListenerContract):
    def __init__(self) -> None:
        self.received: list[SystemEvent] = []

    def on_event(self, event: SystemEvent) -> None:
        self.received.append(event)


def test_event_bus_service_publishes_and_delivers() -> None:
    bus = EventBusService()
    listener = FakeListener()
    bus.subscriber.subscribe("CodeGenerationCompleted", listener)

    ev = bus.publish("CodeGenerationCompleted", "engineer", {"file": "a.py"})
    assert ev.event_type == "CodeGenerationCompleted"
    assert len(listener.received) == 1
    assert listener.received[0].event_id == ev.event_id


def test_event_bus_monitor_tracks_metrics() -> None:
    bus = EventBusService()
    bus.publish("TestEvent", "test", {})
    metrics = bus.monitor.get_metrics()
    assert metrics.published_count == 1
