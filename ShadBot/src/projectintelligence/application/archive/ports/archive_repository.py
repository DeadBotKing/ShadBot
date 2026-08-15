"""
ShadBot Project Intelligence

Archive Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.archive.archive_entry import (
    ArchiveEntry,
)


class ArchiveRepository(ABC):
    """
    Repository contract for intelligence archives.

    Stores historical intelligence executions.
    """

    @abstractmethod
    def save(
        self,
        archive_entry: ArchiveEntry,
    ) -> None:
        """
        Persist archive entry.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        archive_id: UUID,
    ) -> ArchiveEntry | None:
        """
        Retrieve archive by identifier.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest(
        self,
    ) -> ArchiveEntry | None:
        """
        Retrieve latest intelligence archive.
        """
        raise NotImplementedError
