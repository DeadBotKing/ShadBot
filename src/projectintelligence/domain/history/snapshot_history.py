"""
ShadBot Project Intelligence

Snapshot History Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class SnapshotHistory:
    """
    Represents the evolution of a project across snapshots.
    """

    differences: list[SnapshotDifference] = field(
        default_factory=list,
    )

    @property
    def total_snapshots(self) -> int:
        return len(
            self.differences,
        )

    @property
    def total_changes(self) -> int:
        return sum(diff.total_changes for diff in self.differences)
