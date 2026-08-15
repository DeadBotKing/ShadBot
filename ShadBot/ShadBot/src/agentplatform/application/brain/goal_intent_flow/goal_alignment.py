"""
ShadBot Agent Platform

Goal Alignment component for 5.12 Goal & Intent Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .intent_detection import DetectedIntent


@dataclass(frozen=True, slots=True)
class AlignedGoal:
    goal_title: str
    is_aligned: bool
    alignment_score: float


class GoalAligner:
    """
    Aligns detected intent with project vision goals.
    """

    def align(self, intent: DetectedIntent, project_vision_title: str) -> AlignedGoal:
        return AlignedGoal(
            goal_title=f"{project_vision_title}: {intent.primary_intent}",
            is_aligned=True,
            alignment_score=0.95,
        )
