"""
ShadBot Project Intelligence

Snapshot Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class SnapshotDifferenceService:
    """
    Compares two project snapshots.
    """

    def compare(
        self,
        previous: ProjectSnapshot,
        current: ProjectSnapshot,
    ) -> SnapshotDifference:

        difference = SnapshotDifference()

        difference.added_files = sorted(
            set(current.file_hashes) - set(previous.file_hashes),
        )

        difference.removed_files = sorted(
            set(previous.file_hashes) - set(current.file_hashes),
        )

        difference.modified_files = sorted(
            file
            for file in (set(previous.file_hashes) & set(current.file_hashes))
            if previous.file_hashes[file] != current.file_hashes[file]
        )

        return difference
