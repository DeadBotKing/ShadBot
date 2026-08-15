"""
ShadBot Project Intelligence

Test Summary Model
"""

from __future__ import annotations

from dataclasses import dataclass, field

from projectintelligence.domain.testing.models.test_framework import (
    TestFramework,
)


@dataclass(slots=True)
class TestSummary:
    """
    Represents project testing intelligence.
    """

    frameworks: list[TestFramework] = field(
        default_factory=list,
    )

    test_files: int = 0

    status: str = "unknown"
