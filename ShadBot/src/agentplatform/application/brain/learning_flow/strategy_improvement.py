"""
ShadBot Agent Platform

Strategy Improvement component for 5.11 Learning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .pattern_recognition import RecognizedPattern


@dataclass(frozen=True, slots=True)
class StrategyAdjustment:
    preferred_pattern: str
    adjustment_reason: str


class StrategyImprover:
    """
    Adjusts brain planning strategy based on recognized patterns.
    """

    def improve(self, patterns: tuple[RecognizedPattern, ...]) -> StrategyAdjustment:
        if not patterns:
            return StrategyAdjustment(
                preferred_pattern="Standard Plan",
                adjustment_reason="No high confidence pattern recognized.",
            )
        top = sorted(patterns, key=lambda p: p.confidence, reverse=True)[0]
        return StrategyAdjustment(
            preferred_pattern=top.pattern_name,
            adjustment_reason=f"Adopted {top.pattern_name} (Confidence {top.confidence})",
        )
