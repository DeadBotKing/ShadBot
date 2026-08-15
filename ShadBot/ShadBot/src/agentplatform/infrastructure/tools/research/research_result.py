"""
ShadBot Agent Platform

Research Result Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ResearchResult:
    """
    Standard research output.
    """

    success: bool

    query: str

    findings: str

    sources: tuple[str, ...]

    confidence: float

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
