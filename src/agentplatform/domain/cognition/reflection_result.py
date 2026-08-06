"""
ShadBot Agent Platform

Reflection result contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ReflectionResult:
    """
    Output contract from reflection engine.
    """

    success: bool

    summary: str

    lessons: tuple[str, ...] = ()

    failures: tuple[str, ...] = ()

    recommendations: tuple[str, ...] = ()

    confidence: float = 0.0

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    result_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
