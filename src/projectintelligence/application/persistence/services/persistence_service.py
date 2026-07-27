"""
ShadBot Project Intelligence

Persistence Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.persistence.services.context_storage_service import (
    ContextStorageService,
)
from projectintelligence.application.persistence.services.snapshot_storage_service import (
    SnapshotStorageService,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class PersistenceService:
    """
    Coordinates persistence operations for Project Intelligence.
    """

    snapshot_storage: SnapshotStorageService

    context_storage: ContextStorageService

    def save_snapshot(
        self,
        snapshot: ProjectSnapshot,
    ) -> PersistenceResult:
        return self.snapshot_storage.save(
            snapshot,
        )

    def save_context(
        self,
        context: ProjectContext,
    ) -> PersistenceResult:
        return self.context_storage.save(
            context,
        )

    def save_all(
        self,
        snapshot: ProjectSnapshot,
        context: ProjectContext,
    ) -> tuple[
        PersistenceResult,
        PersistenceResult,
    ]:
        snapshot_result = self.save_snapshot(
            snapshot,
        )

        context_result = self.save_context(
            context,
        )

        return (
            snapshot_result,
            context_result,
        )
