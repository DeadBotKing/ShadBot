"""
ShadBot Agent Platform

Goal Lifecycle Transition
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .goal_lifecycle_state import (
    GoalLifecycleState,
)


@dataclass(frozen=True, slots=True)
class GoalTransition:
    """
    Represents a goal state transition.
    """

    goal_id: UUID

    from_state: GoalLifecycleState

    to_state: GoalLifecycleState

    reason: str
