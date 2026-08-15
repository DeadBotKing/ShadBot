"""
ShadBot Agent Platform

Learning event.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class LearningEvent:
    """
    Input event for learning.
    """

    project_id: UUID

    agent: str

    source: str

    content: dict[str, object]

    event_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
