"""
ShadBot Agent Platform

Decision Evaluator component for 5.6 Decision Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .decision_generator import DecisionAlternative


@dataclass(frozen=True, slots=True)
class ScoredDecision:
    alternative: DecisionAlternative
    score: float
    selected: bool


class DecisionEvaluator:
    """
    Evaluates and ranks candidate decision alternatives.
    """

    def evaluate(self, alternatives: Sequence[DecisionAlternative]) -> tuple[ScoredDecision, ...]:
        scored: list[ScoredDecision] = []
        for idx, alt in enumerate(alternatives):
            score = 0.95 if idx == 0 else 0.70
            scored.append(
                ScoredDecision(
                    alternative=alt,
                    score=score,
                    selected=(idx == 0),
                )
            )
        return tuple(scored)
