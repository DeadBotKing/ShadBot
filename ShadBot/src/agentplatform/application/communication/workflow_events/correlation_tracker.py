"""
ShadBot Agent Platform

Workflow Event Correlation component for 8.3 Workflow Events.
"""

from __future__ import annotations

from uuid import UUID
from .workflow_event import WorkflowEvent


class WorkflowCorrelationTracker:
    """
    Links workflow events together by workflow ID to track execution history.
    """

    def __init__(self) -> None:
        self._history: dict[UUID, list[WorkflowEvent]] = {}

    def track(self, event: WorkflowEvent) -> None:
        if event.workflow_id not in self._history:
            self._history[event.workflow_id] = []
        self._history[event.workflow_id].append(event)

    def get_history(self, workflow_id: UUID) -> tuple[WorkflowEvent, ...]:
        return tuple(self._history.get(workflow_id, []))
