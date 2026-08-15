"""
ShadBot Project Intelligence

In Memory History Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.ports.outbound.history_repository import (
    HistoryRepository,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)


class InMemoryHistoryRepository(
    HistoryRepository,
):
    """
    In-memory implementation of history persistence.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            SnapshotHistory,
        ] = {}

    def save(
        self,
        history: SnapshotHistory,
    ) -> None:
        self._storage[history.history_id] = history

    def update(
        self,
        history: SnapshotHistory,
    ) -> None:
        self._storage[history.history_id] = history

    def delete(
        self,
        history_id: UUID,
    ) -> None:
        self._storage.pop(
            history_id,
            None,
        )

    def exists(
        self,
        history_id: UUID,
    ) -> bool:
        return history_id in self._storage

    def get_by_id(
        self,
        history_id: UUID,
    ) -> SnapshotHistory | None:
        return self._storage.get(
            history_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> SnapshotHistory | None:

        histories = [
            history
            for history in self._storage.values()
            if history.project_id == project_id
        ]

        if not histories:
            return None

        return max(
            histories,
            key=lambda item: item.created_at,
        )

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[SnapshotHistory]:

        return [
            history
            for history in self._storage.values()
            if history.project_id == project_id
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
