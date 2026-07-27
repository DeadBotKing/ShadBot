"""
ShadBot Project Intelligence

Snapshot Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class SnapshotRepository(ABC):
    """
    Outbound port for persisting and retrieving project snapshots.

    This contract is implemented by infrastructure adapters
    (SQL Server, SQLite, JSON, etc.) while remaining completely
    independent from any persistence technology.
    """

    @abstractmethod
    def save(self, snapshot: ProjectSnapshot) -> None:
        """Persist a new project snapshot."""

    @abstractmethod
    def update(self, snapshot: ProjectSnapshot) -> None:
        """Update an existing project snapshot."""

    @abstractmethod
    def delete(self, snapshot_id: UUID) -> None:
        """Delete a project snapshot."""

    @abstractmethod
    def exists(self, snapshot_id: UUID) -> bool:
        """Return True if the snapshot exists."""

    @abstractmethod
    def get_by_id(self, snapshot_id: UUID) -> ProjectSnapshot | None:
        """Retrieve a snapshot by its unique identifier."""

    @abstractmethod
    def get_latest(self, project_id: UUID) -> ProjectSnapshot | None:
        """Retrieve the latest snapshot of a project."""

    @abstractmethod
    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectSnapshot]:
        """Return all snapshots belonging to a project."""

    @abstractmethod
    def list_between_dates(
        self,
        project_id: UUID,
        start_date: datetime,
        end_date: datetime,
    ) -> list[ProjectSnapshot]:
        """Return snapshots created within a date range."""

    @abstractmethod
    def count(self, project_id: UUID) -> int:
        """Return the number of snapshots for a project."""
