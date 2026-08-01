"""
ShadBot Project Intelligence

Testing Context Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True)
class TestingContext:
    """
    Domain representation of project testing intelligence.
    """

    project_id: UUID

    context_id: UUID = field(
        default_factory=uuid4,
    )

    detected_frameworks: list[str] = field(
        default_factory=list,
    )

    test_directories: list[str] = field(
        default_factory=list,
    )

    test_files: list[str] = field(
        default_factory=list,
    )

    total_tests: int = 0

    coverage_available: bool = False

    quality_issues: list[str] = field(
        default_factory=list,
    )
