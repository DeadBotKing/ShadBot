"""
ShadBot Agent Platform

Execution Trace Tracking component for 7.7 Runtime Observability.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ExecutionTraceEvent:
    trace_id: UUID
    component: str
    action: str
    status: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class ExecutionTraceTracker:
    """
    Tracks sequential distributed trace events across Runtime components.
    """

    def __init__(self, trace_id: UUID | None = None) -> None:
        self.trace_id = trace_id or uuid4()
        self._events: list[ExecutionTraceEvent] = []

    def log_event(self, component: str, action: str, status: str = "OK") -> ExecutionTraceEvent:
        ev = ExecutionTraceEvent(self.trace_id, component, action, status)
        self._events.append(ev)
        return ev

    def get_events(self) -> tuple[ExecutionTraceEvent, ...]:
        return tuple(self._events)
