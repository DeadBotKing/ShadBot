"""
ShadBot Agent Platform

Goal Completion Result
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .completion_status import (
    CompletionStatus,
)


@dataclass(frozen=True, slots=True)
class GoalCompletionResult:
    """
    Represents completion detection output.
    """

    goal_id: UUID

    status: CompletionStatus

    completed: bool

    message: str

    missing_requirements: tuple[str, ...] = ()
