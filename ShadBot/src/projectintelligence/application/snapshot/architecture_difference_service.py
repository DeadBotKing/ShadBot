"""
ShadBot Project Intelligence

Architecture Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class ArchitectureDifferenceService:
    """
    Compares project architecture trees between snapshots.
    """

    def compare(
        self,
        previous: dict[str, object],
        current: dict[str, object],
        difference: SnapshotDifference,
    ) -> None:

        difference.architecture_changed = previous != current
