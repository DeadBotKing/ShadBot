"""
ShadBot Agent Platform

Execution Test Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ExecutionTestResult:
    """
    Execution validation result.
    """

    capability_id: UUID

    tool_id: UUID

    test_name: str

    passed: bool

    message: str

    execution_time_ms: float = 0.0

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
