"""
Acceptance criteria model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AcceptanceCriteria:
    """
    Validation requirement.
    """

    description: str

    mandatory: bool = True
