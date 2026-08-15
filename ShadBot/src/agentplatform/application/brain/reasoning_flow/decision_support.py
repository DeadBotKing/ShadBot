"""
ShadBot Agent Platform

Decision Support component.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class OptionEvaluation:
    option: str
    feasibility_score: float
    risk_score: float
    recommended: bool


class DecisionSupport:
    """
    Evaluates candidate options to support decision making.
    """

    def evaluate_options(self, options: Sequence[str]) -> tuple[OptionEvaluation, ...]:
        evaluations: list[OptionEvaluation] = []
        for idx, opt in enumerate(options):
            feasibility = 0.9 if idx == 0 else 0.75
            risk = 0.1 if idx == 0 else 0.3
            evaluations.append(
                OptionEvaluation(
                    option=opt,
                    feasibility_score=feasibility,
                    risk_score=risk,
                    recommended=(idx == 0),
                )
            )
        return tuple(evaluations)
