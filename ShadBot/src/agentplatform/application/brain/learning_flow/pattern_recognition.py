"""
ShadBot Agent Platform

Pattern Recognition component for 5.11 Learning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .experience_extraction import ExtractedExperience


@dataclass(frozen=True, slots=True)
class RecognizedPattern:
    pattern_name: str
    occurrence_count: int
    confidence: float


class PatternRecognizer:
    """
    Identifies recurring successful architectural and engineering patterns.
    """

    def recognize(self, experiences: Sequence[ExtractedExperience]) -> tuple[RecognizedPattern, ...]:
        patterns: dict[str, int] = {}
        for exp in experiences:
            if exp.reusable_pattern:
                patterns[exp.reusable_pattern] = patterns.get(exp.reusable_pattern, 0) + 1
        return tuple(
            RecognizedPattern(
                pattern_name=name,
                occurrence_count=count,
                confidence=min(1.0, 0.7 + (count * 0.1)),
            )
            for name, count in patterns.items()
        )
