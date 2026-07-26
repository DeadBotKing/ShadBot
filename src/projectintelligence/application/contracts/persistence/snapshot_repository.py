"""
ShadBot Project Intelligence

Snapshot Repository Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class ISnapshotRepository(ABC):
    """
    Contract for Project Snapshot persistence.
    """

    @abstractmethod
    def save(
        self,
        snapshot: ProjectSnapshot,
    ) -> None:
        """
        Persist a project snapshot.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        snapshot_id: UUID,
    ) -> ProjectSnapshot | None:
        """
        Retrieve snapshot by id.
        """
        raise NotImplementedError