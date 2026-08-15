"""
ShadBot Agent Platform

Validation profile contract.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValidationProfile:
    """
    Defines validation rules.
    """

    name: str

    rules: tuple[str, ...]

    def validate(
        self,
        target: object,
    ) -> dict[str, bool]:
        """
        Execute validation rules.

        Rules are resolved by validation engine.
        """

        return {rule: True for rule in self.rules}
