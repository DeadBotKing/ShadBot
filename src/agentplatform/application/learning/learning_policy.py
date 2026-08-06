"""
ShadBot Agent Platform

Learning policy.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.learning import (
    LearningEvent,
)


@dataclass(frozen=True, slots=True)
class LearningPolicy:
    """
    Defines rules for accepting learning signals.

    Responsibilities
    ----------------
    - Decide whether an event is learnable
    - Define confidence calculation
    - Control learning thresholds

    Does not:
    - Store memories
    - Execute learning
    - Modify agents
    """

    minimum_content_size: int = 1

    minimum_confidence: float = 0.70

    def should_learn(
        self,
        event: LearningEvent,
    ) -> bool:
        """
        Determine if event contains enough
        information for learning.
        """

        if not event.content:
            return False

        return len(event.content) >= self.minimum_content_size

    def calculate_confidence(
        self,
        event: LearningEvent,
    ) -> float:
        """
        Calculate initial learning confidence.
        """

        confidence = event.content.get(
            "confidence",
            1.0,
        )

        if not isinstance(
            confidence,
            (int, float),
        ):
            return 0.0

        value = float(confidence)

        if value < 0:
            return 0.0

        if value > 1:
            return 1.0

        return value

    def is_valid_confidence(
        self,
        confidence: float,
    ) -> bool:
        """
        Validate confidence threshold.
        """

        return confidence >= self.minimum_confidence
