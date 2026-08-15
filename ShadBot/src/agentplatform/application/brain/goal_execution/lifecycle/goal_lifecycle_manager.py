"""
ShadBot Agent Platform

Goal Lifecycle Manager
"""

from __future__ import annotations

from uuid import UUID

from .goal_lifecycle_state import (
    GoalLifecycleState,
)
from .goal_transition import (
    GoalTransition,
)


class GoalLifecycleManager:
    """
    Controls goal lifecycle transitions.
    """

    _allowed_transitions = {
        GoalLifecycleState.CREATED: {
            GoalLifecycleState.UNDERSTANDING,
        },
        GoalLifecycleState.UNDERSTANDING: {
            GoalLifecycleState.PLANNING,
            GoalLifecycleState.FAILED,
        },
        GoalLifecycleState.PLANNING: {
            GoalLifecycleState.EXECUTING,
            GoalLifecycleState.FAILED,
        },
        GoalLifecycleState.EXECUTING: {
            GoalLifecycleState.VALIDATING,
            GoalLifecycleState.FAILED,
        },
        GoalLifecycleState.VALIDATING: {
            GoalLifecycleState.COMPLETED,
            GoalLifecycleState.FAILED,
        },
        GoalLifecycleState.COMPLETED: set(),
        GoalLifecycleState.FAILED: set(),
    }

    def can_transition(
        self,
        *,
        current: GoalLifecycleState,
        target: GoalLifecycleState,
    ) -> bool:
        """
        Validate lifecycle transition.
        """

        return target in (
            self._allowed_transitions.get(
                current,
                set(),
            )
        )

    def transition(
        self,
        *,
        goal_id: UUID,
        current: GoalLifecycleState,
        target: GoalLifecycleState,
        reason: str,
    ) -> GoalTransition:
        """
        Execute lifecycle transition.
        """

        if not self.can_transition(
            current=current,
            target=target,
        ):
            raise ValueError(
                f"Invalid goal transition: " f"{current.value} -> {target.value}"
            )

        return GoalTransition(
            goal_id=goal_id,
            from_state=current,
            to_state=target,
            reason=reason,
        )
