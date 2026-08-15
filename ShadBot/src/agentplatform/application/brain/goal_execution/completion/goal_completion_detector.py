"""
ShadBot Agent Platform

Goal Completion Detector
"""

from __future__ import annotations

from uuid import UUID

from .completion_status import (
    CompletionStatus,
)
from .goal_completion_result import (
    GoalCompletionResult,
)


class GoalCompletionDetector:
    """
    Detects whether goal execution is complete.
    """

    def detect(
        self,
        *,
        goal_id: UUID,
        progress: float,
        validation_passed: bool,
        required_items: tuple[str, ...],
        completed_items: tuple[str, ...],
    ) -> GoalCompletionResult:
        """
        Evaluate goal completion.
        """

        missing = tuple(item for item in required_items if item not in completed_items)

        if missing:

            return GoalCompletionResult(
                goal_id=goal_id,
                status=CompletionStatus.IN_PROGRESS,
                completed=False,
                message=("Goal has unfinished requirements"),
                missing_requirements=missing,
            )

        if not validation_passed:

            return GoalCompletionResult(
                goal_id=goal_id,
                status=CompletionStatus.BLOCKED,
                completed=False,
                message=("Validation has not passed"),
            )

        if progress < 100:

            return GoalCompletionResult(
                goal_id=goal_id,
                status=CompletionStatus.IN_PROGRESS,
                completed=False,
                message=("Goal execution is still progressing"),
            )

        return GoalCompletionResult(
            goal_id=goal_id,
            status=CompletionStatus.COMPLETED,
            completed=True,
            message=("Goal completed successfully"),
        )
