"""
ShadBot Agent Platform

Decision Output component for 5.6 Decision Flow.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4
from .decision_approval import DecisionApprovalResult
from .decision_evaluator import ScoredDecision


@dataclass(frozen=True, slots=True)
class FinalDecisionPackage:
    decision_id: UUID
    selected_title: str
    score: float
    approved: bool
    rationale: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class DecisionOutput:
    """
    Formats the final decision into an enterprise decision package.
    """

    def format(self, scored: ScoredDecision, approval: DecisionApprovalResult) -> FinalDecisionPackage:
        return FinalDecisionPackage(
            decision_id=scored.alternative.alternative_id,
            selected_title=scored.alternative.title,
            score=scored.score,
            approved=approval.approved,
            rationale=approval.reason,
        )
