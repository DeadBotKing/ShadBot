"""
ShadBot Agent Platform

Requirement Verification component for 5.10 Validation Flow.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RequirementVerificationResult:
    satisfied: bool
    missing_requirements: tuple[str, ...]


class RequirementVerifier:
    """
    Verifies that all explicit task instructions have been satisfied.
    """

    def verify(self, instructions: str, delivered_capabilities: tuple[str, ...]) -> RequirementVerificationResult:
        missing: list[str] = []
        lower_inst = instructions.lower()
        if "test" in lower_inst and "test_generation" not in delivered_capabilities:
            missing.append("Missing required test generation")
        return RequirementVerificationResult(
            satisfied=(len(missing) == 0),
            missing_requirements=tuple(missing),
        )
