"""
ShadBot Project Intelligence

History Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)


class HistoryRepository(ABC):
    """
    Outbound port for persisting and retrieving project history.
    """

    @abstractmethod
    def save(
        self,
        history: SnapshotHistory,
    ) -> None:
        """
        Persist project history.
        """

    @abstractmethod
    def update(
        self,
        history: SnapshotHistory,
    ) -> None:
        """
        Update existing project history.
        """

    @abstractmethod
    def delete(
        self,
        history_id: UUID,
    ) -> None:
        """
        Delete project history.
        """

    @abstractmethod
    def exists(
        self,
        history_id: UUID,
    ) -> bool:
        """
        Check whether history exists.
        """

    @abstractmethod
    def get_by_id(
        self,
        history_id: UUID,
    ) -> SnapshotHistory | None:
        """
        Retrieve history by identifier.
        """

    @abstractmethod
    def get_latest(
        self,
        project_id: UUID,
    ) -> SnapshotHistory | None:
        """
        Retrieve latest project history.
        """

    @abstractmethod
    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[SnapshotHistory]:
        """
        Retrieve all histories of a project.
        """

    @abstractmethod
    def count(
        self,
        project_id: UUID,
    ) -> int:
        """
        Count stored histories.
        """