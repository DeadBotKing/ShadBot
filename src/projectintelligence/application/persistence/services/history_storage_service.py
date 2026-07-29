"""
ShadBot Project Intelligence

History Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.ports.outbound.history_repository import (
    HistoryRepository,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)


@dataclass(slots=True)
class HistoryStorageService:
    """
    Coordinates persistence of project history.
    """

    repository: HistoryRepository

    def save(
        self,
        history: SnapshotHistory,
    ) -> PersistenceResult:
        self.repository.save(
            history,
        )

        return PersistenceResult.succeeded(
            operation="save",
            entity="SnapshotHistory",
            identifier=str(history.history_id),
            message="Project history stored successfully.",
        )
