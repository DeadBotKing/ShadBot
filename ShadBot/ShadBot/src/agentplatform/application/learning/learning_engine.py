"""
ShadBot Agent Platform

Learning Engine.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.learning import (
    LearningEvent,
    LearningResult,
    LearningStatus,
)


@dataclass(slots=True)
class LearningEngine:
    """
    Core engine responsible for transforming
    execution feedback into reusable knowledge.

    Responsibilities
    ----------------
    - Normalize learning events
    - Produce deterministic learning results
    - Never perform persistence
    - Never communicate with LLM
    - Never access infrastructure
    """

    minimum_confidence: float = 0.70

    def process(
        self,
        event: LearningEvent,
        learned_items: tuple[str, ...],
        confidence: float,
        summary: str,
    ) -> LearningResult:
        """
        Produce immutable learning result.
        """

        status = (
            LearningStatus.COMPLETED
            if confidence >= self.minimum_confidence
            else LearningStatus.FAILED
        )

        return LearningResult(
            status=status,
            learned_items=learned_items,
            confidence=confidence,
            summary=summary,
        )
