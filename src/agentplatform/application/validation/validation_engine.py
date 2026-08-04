"""
ShadBot Agent Platform

Validation engine.
"""

from __future__ import annotations

from agentplatform.application.validation.validation_result import (
    ValidationResult,
)
from agentplatform.domain.validation import (
    ValidationProfile,
)


class ValidationEngine:
    """
    Executes validation profiles.
    """

    def validate(
        self,
        profile: ValidationProfile,
        target: object,
    ) -> ValidationResult:
        """
        Execute validation rules.
        """

        results = profile.validate(
            target,
        )

        failures = [name for name, passed in results.items() if not passed]

        return ValidationResult(
            passed=len(failures) == 0,
            results=results,
            failures=failures,
        )
