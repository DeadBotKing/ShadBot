"""
ShadBot Agent Platform

Project evolution model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .evolution_change import EvolutionChange


@dataclass(frozen=True, slots=True)
class ProjectEvolution:
    """
    Difference between two project visions.
    """

    project_id: UUID

    previous_version: str

    current_version: str

    changes: tuple[EvolutionChange, ...]

    impact_summary: str

    evolution_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
