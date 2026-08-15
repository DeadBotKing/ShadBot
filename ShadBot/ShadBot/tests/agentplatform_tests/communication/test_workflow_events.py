"""
ShadBot Agent Platform

Unit tests for 8.3 Workflow Events.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.communication.workflow_events import (
    WorkflowEvent,
    WorkflowEventsService,
)


def test_workflow_events_service_emits_and_correlates() -> None:
    service = WorkflowEventsService()
    wid = uuid4()
    triggered: list[WorkflowEvent] = []
    service.trigger_mgr.register_trigger("COMPLETED", lambda ev: triggered.append(ev))

    ev, count = service.emit(wid, "COMPLETED", 1, {"data": "done"})
    assert count == 1
    assert len(triggered) == 1
    assert len(service.tracker.get_history(wid)) == 1
