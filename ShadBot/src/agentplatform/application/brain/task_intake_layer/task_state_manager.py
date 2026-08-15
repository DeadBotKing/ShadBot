"""
ShadBot Agent Platform

Task State Manager component for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class TaskIntakeState:
    task_id: UUID
    status: str
    last_updated: str


class TaskStateManager:
    """
    Manages task intake state across lifecycle.
    """

    def __init__(self) -> None:
        self._states: dict[UUID, TaskIntakeState] = {}

    def set_status(self, task_id: UUID, status: str) -> TaskIntakeState:
        state = TaskIntakeState(
            task_id=task_id,
            status=status,
            last_updated=datetime.now(timezone.utc).isoformat(),
        )
        self._states[task_id] = state
        return state

    def get_status(self, task_id: UUID) -> TaskIntakeState | None:
        return self._states.get(task_id)
