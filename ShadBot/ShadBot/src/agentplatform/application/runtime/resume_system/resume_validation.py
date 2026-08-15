"""
ShadBot Agent Platform

Resume Validation component for 7.6 Resume System.
"""

from __future__ import annotations

from dataclasses import dataclass
from .recovery_engine import ExecutionRecoveryState


@dataclass(frozen=True, slots=True)
class ResumeValidationResult:
    valid_resume: bool
    notes: str


class ResumeValidator:
    """
    Validates if a resumed execution recovery state is ready for continuation.
    """

    def validate(self, state: ExecutionRecoveryState) -> ResumeValidationResult:
        if not state.is_recovered:
            return ResumeValidationResult(False, "Execution recovery state is not marked as recovered.")
        return ResumeValidationResult(True, f"Valid resume from step {state.resumed_step}.")
