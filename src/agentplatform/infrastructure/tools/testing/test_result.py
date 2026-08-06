"""
ShadBot Agent Platform

Test Result Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class TestResult:
    """
    Standard test execution result.
    """

    success: bool

    exit_code: int

    output: str

    errors: str

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
