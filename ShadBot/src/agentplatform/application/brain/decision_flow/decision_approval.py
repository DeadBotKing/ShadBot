"""
ShadBot Agent Platform

Decision Approval component for 5.6 Decision Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .decision_evaluator import ScoredDecision


@dataclass(frozen=True, slots=True)
class DecisionApprovalResult:
    approved: bool
    reason: str
    minimum_score_threshold: float = 0.80


class DecisionApproval:
    """
    Validates if the selected decision alternative satisfies quality threshold.
    """

    def approve(self, decision: ScoredDecision) -> DecisionApprovalResult:
        if decision.score >= 0.80:
            return DecisionApprovalResult(
                approved=True,
                reason=f"Score {decision.score} satisfies threshold.",
            )
        return DecisionApprovalResult(
            approved=False,
            reason=f"Score {decision.score} is below 0.80 threshold.",
        )
