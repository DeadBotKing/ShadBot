"""
ShadBot Agent Platform

Tool Test Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ToolTestResult:
    """
    Result of tool validation.
    """

    tool_id: UUID

    test_name: str

    passed: bool

    message: str

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
