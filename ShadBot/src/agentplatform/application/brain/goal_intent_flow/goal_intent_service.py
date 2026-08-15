"""
ShadBot Agent Platform

Unified service for 5.12 Goal & Intent Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .goal_alignment import AlignedGoal, GoalAligner
from .intent_correction import CorrectedIntent, IntentCorrector
from .intent_detection import DetectedIntent, IntentDetector
from .priority_management import PriorityAllocation, PriorityManager


@dataclass(frozen=True, slots=True)
class GoalIntentPackage:
    intent: DetectedIntent
    aligned: AlignedGoal
    priority: PriorityAllocation
    correction: CorrectedIntent


class GoalIntentService:
    """
    Orchestrates intent detection, goal alignment, prioritization, and correction.
    """

    def __init__(
        self,
        detector: IntentDetector | None = None,
        aligner: GoalAligner | None = None,
        manager: PriorityManager | None = None,
        corrector: IntentCorrector | None = None,
    ) -> None:
        self._detector = detector or IntentDetector()
        self._aligner = aligner or GoalAligner()
        self._manager = manager or PriorityManager()
        self._corrector = corrector or IntentCorrector()

    def process(self, instructions: str, project_title: str = "Project") -> GoalIntentPackage:
        raw_intent = self._detector.detect(instructions)
        corr = self._corrector.correct(raw_intent)
        aligned = self._aligner.align(corr.corrected_intent, project_title)
        prio = self._manager.prioritize(aligned.is_aligned)
        return GoalIntentPackage(
            intent=corr.corrected_intent,
            aligned=aligned,
            priority=prio,
            correction=corr,
        )
