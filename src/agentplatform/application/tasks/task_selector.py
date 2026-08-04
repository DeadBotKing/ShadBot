"""
ShadBot Agent Platform

Task selector.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SelectableTask:
    """
    Task candidate.
    """

    id: str

    phase: str

    title: str

    task_type: str

    priority: str

    status: str


class TaskSelector:
    """
    Selects next executable task.
    """

    def select_next(
        self,
        tasks: list[SelectableTask],
        phase_id: str,
    ) -> SelectableTask | None:
        """
        Select highest priority pending task
        from active phase.
        """

        candidates = [
            task
            for task in tasks
            if task.phase == phase_id and task.status == "pending"
        ]

        if not candidates:
            return None

        priority_order = {
            "critical": 0,
            "high": 1,
            "medium": 2,
            "low": 3,
        }

        return sorted(
            candidates,
            key=lambda task: priority_order.get(
                task.priority,
                99,
            ),
        )[0]
