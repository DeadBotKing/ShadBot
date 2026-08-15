"""
ShadBot Agent Platform

Validation rule domain model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True, slots=True)
class ValidationRule:
    """
    Single validation rule definition.
    """

    name: str
    description: str
    validator: Callable[[object], bool]

    def validate(
        self,
        target: object,
    ) -> bool:
        """
        Execute validation rule.
        """

        return self.validator(target)
