"""
ShadBot Agent Platform

Validation profile domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.validation.validation_rule import (
    ValidationRule,
)


@dataclass(frozen=True, slots=True)
class ValidationProfile:
    """
    Collection of validation rules for a specific domain.
    """

    name: str

    rules: list[ValidationRule] = field(
        default_factory=list,
    )

    def validate(
        self,
        target: object,
    ) -> dict[str, bool]:
        """
        Execute all validation rules.
        """

        return {rule.name: rule.validate(target) for rule in self.rules}
