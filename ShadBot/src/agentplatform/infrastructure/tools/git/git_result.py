"""
ShadBot Agent Platform

Git Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class GitResult:
    """
    Standard git execution result.
    """

    success: bool

    exit_code: int

    output: str

    error: str

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
