"""
ShadBot Agent Platform

Recovery Validation component for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from .retry_management import RetryDecision


@dataclass(frozen=True, slots=True)
class RecoveryValidationResult:
    valid_recovery_plan: bool
    message: str


class RecoveryValidator:
    """
    Validates if the recovery plan is valid and within budget limits.
    """

    def validate(self, retry: RetryDecision) -> RecoveryValidationResult:
        if retry.attempt_number > 5:
            return RecoveryValidationResult(False, "Max retry ceiling exceeded.")
        return RecoveryValidationResult(True, "Recovery plan is valid.")
