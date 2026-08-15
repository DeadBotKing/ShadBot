"""
ShadBot Agent Platform

Handoff History Tracking component for 6.4 Agent Handoff.
"""

from __future__ import annotations

from uuid import UUID
from .transition_manager import AgentTransitionRecord


class HandoffHistoryTracker:
    """
    Tracks and retrieves agent handoff history by task ID.
    """

    def __init__(self) -> None:
        self._history: dict[UUID, list[AgentTransitionRecord]] = {}

    def add_record(self, record: AgentTransitionRecord) -> None:
        if record.task_id not in self._history:
            self._history[record.task_id] = []
        self._history[record.task_id].append(record)

    def get_history(self, task_id: UUID) -> tuple[AgentTransitionRecord, ...]:
        return tuple(self._history.get(task_id, []))
