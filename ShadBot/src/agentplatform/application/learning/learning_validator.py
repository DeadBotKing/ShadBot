"""
ShadBot Agent Platform

Learning validator.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.learning import (
    LearningResult,
    LearningStatus,
)


@dataclass(slots=True)
class LearningValidator:
    """
    Validates generated learning results.

    Responsibilities
    ----------------
    - Validate learning completeness
    - Reject invalid knowledge
    - Ensure confidence integrity

    Does not:
    - Persist knowledge
    - Modify models
    - Execute agents
    """

    minimum_confidence: float = 0.70

    def validate(
        self,
        result: LearningResult,
    ) -> bool:
        """
        Validate learning result.
        """

        if result.status != LearningStatus.COMPLETED:
            return False

        if result.confidence < self.minimum_confidence:
            return False

        if not result.learned_items:
            return False

        return True

    def normalize_confidence(
        self,
        confidence: float,
    ) -> float:
        """
        Keep confidence between 0 and 1.
        """

        if confidence < 0:
            return 0.0

        if confidence > 1:
            return 1.0

        return float(confidence)
