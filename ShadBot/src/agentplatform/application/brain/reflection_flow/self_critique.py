"""
ShadBot Agent Platform

Self Critique component for 5.9 Reflection Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .execution_review import ExecutionReviewResult


@dataclass(frozen=True, slots=True)
class SelfCritiqueResult:
    score: float
    critique_notes: str


class SelfCritiquer:
    """
    Critiques the Brain's own planning and decision effectiveness.
    """

    def critique(self, review: ExecutionReviewResult) -> SelfCritiqueResult:
        if review.total_executed == 0:
            return SelfCritiqueResult(0.0, "No execution attempted.")
        score = review.success_count / review.total_executed
        notes = "Planning was highly effective." if score >= 0.8 else "Plan requires strategy revision."
        return SelfCritiqueResult(score=round(score, 2), critique_notes=notes)
