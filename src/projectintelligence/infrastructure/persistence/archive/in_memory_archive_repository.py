"""
ShadBot Project Intelligence

In Memory Archive Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.archive.ports.archive_repository import (
    ArchiveRepository,
)
from projectintelligence.domain.archive.archive_entry import (
    ArchiveEntry,
)


class InMemoryArchiveRepository(ArchiveRepository):
    """
    In memory implementation of archive storage.

    Used for runtime execution and testing.
    """

    def __init__(self) -> None:
        self._archives: dict[UUID, ArchiveEntry] = {}

    def save(
        self,
        archive_entry: ArchiveEntry,
    ) -> None:
        self._archives[archive_entry.archive_id] = archive_entry

    def get_by_id(
        self,
        archive_id: UUID,
    ) -> ArchiveEntry | None:
        return self._archives.get(
            archive_id,
        )

    def get_latest(
        self,
    ) -> ArchiveEntry | None:

        if not self._archives:
            return None

        return next(
            reversed(
                self._archives.values(),
            ),
        )
