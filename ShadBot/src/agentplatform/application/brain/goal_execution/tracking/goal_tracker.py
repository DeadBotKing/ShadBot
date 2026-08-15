"""
ShadBot Agent Platform

Goal Tracker
"""

from __future__ import annotations

from uuid import UUID

from .goal_progress import (
    GoalProgress,
)
from .goal_tracking_event import (
    GoalTrackingEvent,
)


class GoalTracker:
    """
    Tracks goal execution state.
    """

    def __init__(
        self,
    ) -> None:

        self._events: list[GoalTrackingEvent] = []

    def update_progress(
        self,
        *,
        goal_id: UUID,
        stage: str,
        percentage: float,
        message: str,
        completed_steps: tuple[str, ...] = (),
        remaining_steps: tuple[str, ...] = (),
    ) -> GoalProgress:
        """
        Update goal progress.
        """

        if percentage < 0 or percentage > 100:
            raise ValueError("Progress must be between 0 and 100")

        event = GoalTrackingEvent(
            goal_id=goal_id,
            stage=stage,
            message=message,
            progress=percentage,
        )

        self._events.append(
            event,
        )

        return GoalProgress(
            goal_id=goal_id,
            percentage=percentage,
            current_stage=stage,
            completed_steps=completed_steps,
            remaining_steps=remaining_steps,
        )

    def history(
        self,
        goal_id: UUID,
    ) -> tuple[GoalTrackingEvent, ...]:
        """
        Return goal tracking history.
        """

        return tuple(event for event in self._events if event.goal_id == goal_id)
