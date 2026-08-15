"""
ShadBot Agent Platform

Goal Tracking Event
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class GoalTrackingEvent:
    """
    Goal execution tracking history event.
    """

    goal_id: UUID

    stage: str

    message: str

    progress: float

    event_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
