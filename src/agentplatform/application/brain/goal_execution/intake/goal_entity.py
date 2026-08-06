"""
ShadBot Agent Platform

Goal Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class GoalStatus(str, Enum):
    """
    Goal lifecycle states.
    """

    CREATED = "created"

    UNDERSTANDING = "understanding"

    PLANNING = "planning"

    EXECUTING = "executing"

    VALIDATING = "validating"

    COMPLETED = "completed"

    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class Goal:
    """
    Brain execution goal.
    """

    project_id: UUID

    title: str

    description: str

    source: str

    status: GoalStatus = GoalStatus.CREATED

    goal_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
