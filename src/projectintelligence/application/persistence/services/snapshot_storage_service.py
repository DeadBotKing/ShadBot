"""
ShadBot Project Intelligence

Snapshot Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.ports.outbound.snapshot_repository import (
    SnapshotRepository,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class SnapshotStorageService:
    """
    Application service responsible for snapshot persistence.
    """

    repository: SnapshotRepository

    def save(
        self,
        snapshot: ProjectSnapshot,
    ) -> PersistenceResult:
        self.repository.save(snapshot)

        return PersistenceResult.succeeded(
            operation="save",
            entity="ProjectSnapshot",
            identifier=str(snapshot.snapshot_id),
            message="Snapshot stored successfully.",
        )

    def update(
        self,
        snapshot: ProjectSnapshot,
    ) -> PersistenceResult:
        self.repository.update(snapshot)

        return PersistenceResult.succeeded(
            operation="update",
            entity="ProjectSnapshot",
            identifier=str(snapshot.snapshot_id),
            message="Snapshot updated successfully.",
        )

    def delete(
        self,
        snapshot: ProjectSnapshot,
    ) -> PersistenceResult:
        self.repository.delete(snapshot.snapshot_id)

        return PersistenceResult.succeeded(
            operation="delete",
            entity="ProjectSnapshot",
            identifier=str(snapshot.snapshot_id),
            message="Snapshot deleted successfully.",
        )
