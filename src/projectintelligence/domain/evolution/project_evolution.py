"""
ShadBot Project Intelligence

Project Evolution
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from projectintelligence.domain.evolution.evolution_change import (
    EvolutionChange,
)


@dataclass(frozen=True, slots=True)
class ProjectEvolution:
    """
    Represents evolution between two project snapshots.
    """

    project_id: UUID

    previous_snapshot_id: UUID

    current_snapshot_id: UUID

    evolution_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    changes: tuple[EvolutionChange, ...] = field(
        default_factory=tuple,
    )
