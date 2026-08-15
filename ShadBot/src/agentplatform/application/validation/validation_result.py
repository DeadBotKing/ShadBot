"""
ShadBot Agent Platform

Validation result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """
    Result produced by validation execution.
    """

    passed: bool

    results: dict[str, bool] = field(
        default_factory=dict,
    )

    failures: list[str] = field(
        default_factory=list,
    )
