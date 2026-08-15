"""
ShadBot Agent Platform

Intent Detection component for 5.12 Goal & Intent Flow.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DetectedIntent:
    primary_intent: str
    confidence: float
    implicit_requirements: tuple[str, ...]


class IntentDetector:
    """
    Detects underlying user intent from raw instructions.
    """

    def detect(self, instructions: str) -> DetectedIntent:
        lower = instructions.lower()
        if "test" in lower or "verify" in lower:
            intent = "Verification & Quality Assurance"
            reqs = ("generate_unit_tests", "check_coverage")
        elif "design" in lower or "architecture" in lower:
            intent = "System Architecture Design"
            reqs = ("define_contracts", "specify_layers")
        else:
            intent = "Software Implementation"
            reqs = ("adhere_to_clean_architecture", "pass_quality_gate")
        return DetectedIntent(
            primary_intent=intent,
            confidence=0.90,
            implicit_requirements=reqs,
        )
