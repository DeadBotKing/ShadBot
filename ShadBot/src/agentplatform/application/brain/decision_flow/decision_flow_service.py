"""
ShadBot Agent Platform

Unified service for 5.6 Decision Flow.
"""

from __future__ import annotations

from typing import Sequence
from .decision_approval import DecisionApproval
from .decision_evaluator import DecisionEvaluator
from .decision_generator import DecisionGenerator
from .decision_output import DecisionOutput, FinalDecisionPackage


class DecisionFlowService:
    """
    Orchestrates generation, evaluation, approval, and output of decisions.
    """

    def __init__(
        self,
        generator: DecisionGenerator | None = None,
        evaluator: DecisionEvaluator | None = None,
        approval: DecisionApproval | None = None,
        output: DecisionOutput | None = None,
    ) -> None:
        self._generator = generator or DecisionGenerator()
        self._evaluator = evaluator or DecisionEvaluator()
        self._approval = approval or DecisionApproval()
        self._output = output or DecisionOutput()

    def decide(self, candidate_options: Sequence[str]) -> FinalDecisionPackage:
        alts = self._generator.generate(candidate_options)
        scored = self._evaluator.evaluate(alts)
        selected = [s for s in scored if s.selected]
        choice = selected[0] if selected else scored[0]
        approval_res = self._approval.approve(choice)
        return self._output.format(choice, approval_res)
