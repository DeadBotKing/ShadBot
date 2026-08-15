"""
ShadBot Project Intelligence

Snapshot History Service
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from projectintelligence.application.ports.outbound.snapshot_repository import (
    SnapshotRepository,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class SnapshotHistoryService:
    """
    Provides historical snapshot operations for the
    Project Intelligence application layer.
    """

    repository: SnapshotRepository

    def get_latest_snapshot(
        self,
        project_id: UUID,
    ) -> ProjectSnapshot | None:
        """
        Return the latest snapshot of the project.
        """

        return self.repository.get_latest(
            project_id,
        )

    def has_previous_snapshot(
        self,
        project_id: UUID,
    ) -> bool:
        """
        Determine whether the project already has
        persisted snapshots.
        """

        return (
            self.repository.count(
                project_id,
            )
            > 0
        )

    def snapshot_count(
        self,
        project_id: UUID,
    ) -> int:
        """
        Return the number of stored snapshots.
        """

        return self.repository.count(
            project_id,
        )
