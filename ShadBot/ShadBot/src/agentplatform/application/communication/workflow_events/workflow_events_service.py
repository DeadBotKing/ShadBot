"""
ShadBot Agent Platform

Unified service for 8.3 Workflow Events.
"""

from __future__ import annotations

from typing import Any, Callable
from uuid import UUID, uuid4
from .correlation_tracker import WorkflowCorrelationTracker
from .trigger_manager import WorkflowTriggerManager
from .workflow_event import WorkflowEvent


class WorkflowEventsService:
    """
    Orchestrates workflow event creation, correlation tracking, trigger reaction, and recovery.
    """

    def __init__(
        self,
        trigger_mgr: WorkflowTriggerManager | None = None,
        tracker: WorkflowCorrelationTracker | None = None,
    ) -> None:
        self.trigger_mgr = trigger_mgr or WorkflowTriggerManager()
        self.tracker = tracker or WorkflowCorrelationTracker()

    def emit(
        self,
        workflow_id: UUID,
        state: str,
        step: int,
        payload: dict[str, Any],
    ) -> tuple[WorkflowEvent, int]:
        event = WorkflowEvent(
            event_id=uuid4(),
            workflow_id=workflow_id,
            state=state.upper(),
            step_number=step,
            payload=payload,
        )
        self.tracker.track(event)
        handlers_triggered = self.trigger_mgr.trigger(event)
        return event, handlers_triggered
