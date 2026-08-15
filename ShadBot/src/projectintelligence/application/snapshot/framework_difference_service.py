"""
ShadBot Project Intelligence

Framework Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class FrameworkDifferenceService:
    """
    Compares detected frameworks between snapshots.
    """

    def compare(
        self,
        previous: list[str],
        current: list[str],
        difference: SnapshotDifference,
    ) -> None:

        difference.framework_changes = sorted(
            set(previous).symmetric_difference(
                current,
            ),
        )
