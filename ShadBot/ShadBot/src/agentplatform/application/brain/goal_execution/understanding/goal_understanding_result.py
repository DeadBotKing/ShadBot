"""
ShadBot Agent Platform

Goal Understanding Result
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .goal_analysis import GoalAnalysis


@dataclass(frozen=True, slots=True)
class GoalUnderstandingResult:
    """
    Result of goal understanding process.
    """

    goal_id: UUID

    understood: bool

    analysis: GoalAnalysis | None

    message: str
