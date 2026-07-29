"""
ShadBot Project Intelligence

In Memory Snapshot Repository
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from projectintelligence.application.ports.outbound.snapshot_repository import (
    SnapshotRepository,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class InMemorySnapshotRepository(
    SnapshotRepository,
):
    """
    In-memory implementation of snapshot persistence.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            ProjectSnapshot,
        ] = {}

    def save(
        self,
        snapshot: ProjectSnapshot,
    ) -> None:
        self._storage[snapshot.snapshot_id] = snapshot

    def update(
        self,
        snapshot: ProjectSnapshot,
    ) -> None:
        self._storage[snapshot.snapshot_id] = snapshot

    def delete(
        self,
        snapshot_id: UUID,
    ) -> None:
        self._storage.pop(
            snapshot_id,
            None,
        )

    def exists(
        self,
        snapshot_id: UUID,
    ) -> bool:
        return snapshot_id in self._storage

    def get_by_id(
        self,
        snapshot_id: UUID,
    ) -> ProjectSnapshot | None:
        return self._storage.get(
            snapshot_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectSnapshot | None:
        snapshots = [
            snapshot
            for snapshot in self._storage.values()
            if snapshot.project_id == project_id
        ]

        if not snapshots:
            return None

        return max(
            snapshots,
            key=lambda item: item.created_at,
        )

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectSnapshot]:
        return [
            snapshot
            for snapshot in self._storage.values()
            if snapshot.project_id == project_id
        ]

    def count(
        self,
        project_id: UUID,
    ) -> int:
        return len(
            self.list_by_project(
                project_id,
            ),
        )

    def list_between_dates(
        self,
        project_id: UUID,
        start_date: datetime,
        end_date: datetime,
    ) -> list[ProjectSnapshot]:
        return [
            snapshot
            for snapshot in self._storage.values()
            if (
                snapshot.project_id == project_id
                and start_date <= snapshot.created_at <= end_date
            )
        ]
