"""
ShadBot Agent Platform

Validation engine.
"""

from __future__ import annotations

from agentplatform.domain.validation import (
    ValidationProfile,
    ValidationRequest,
)

from .validation_result import ValidationResult


class ValidationEngine:
    """
    Executes validation workflows.
    """

    def validate(
        self,
        request: ValidationRequest,
        profile: ValidationProfile,
    ) -> ValidationResult:
        """
        Execute validation profile against target.
        """

        results = profile.validate(
            request.target,
        )

        failures = [name for name, passed in results.items() if not passed]

        return ValidationResult(
            passed=len(failures) == 0,
            results=results,
            failures=failures,
        )
