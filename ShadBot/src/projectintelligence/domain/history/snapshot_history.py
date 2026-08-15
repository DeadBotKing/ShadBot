"""
ShadBot Project Intelligence

Snapshot History Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class SnapshotHistory:
    """
    Represents the evolution history of a project.
    """

    history_id: UUID

    project_id: UUID

    created_at: datetime

    differences: list[SnapshotDifference] = field(
        default_factory=list,
    )

    @property
    def total_snapshots(self) -> int:
        return len(self.differences)

    @property
    def total_changes(self) -> int:
        return sum(difference.total_changes for difference in self.differences)
