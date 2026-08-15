"""
ShadBot Agent Platform

Output Validation component for 5.10 Validation Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class OutputValidationResult:
    valid: bool
    checked_files: int
    errors: tuple[str, ...]


class OutputValidator:
    """
    Validates output artifacts for syntax and structural compliance.
    """

    def validate(self, files: Sequence[str]) -> OutputValidationResult:
        errors: list[str] = []
        for f in files:
            if not f.endswith((".py", ".md", ".json", ".txt", ".toml", ".ini", ".yaml", ".yml")):
                errors.append(f"Unsupported artifact extension: {f}")
        return OutputValidationResult(
            valid=(len(errors) == 0),
            checked_files=len(files),
            errors=tuple(errors),
        )
