"""
ShadBot Project Intelligence

Snapshot History Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.snapshot.snapshot_difference_service import (
    SnapshotDifferenceService,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class SnapshotHistoryService:
    """
    Builds project history from ordered snapshots.
    """

    difference_service: SnapshotDifferenceService

    def build(
        self,
        snapshots: list[ProjectSnapshot],
    ) -> SnapshotHistory:

        history = SnapshotHistory()

        for previous, current in zip(
            snapshots,
            snapshots[1:],
        ):
            history.differences.append(
                self.difference_service.compare(
                    previous,
                    current,
                ),
            )

        return history
