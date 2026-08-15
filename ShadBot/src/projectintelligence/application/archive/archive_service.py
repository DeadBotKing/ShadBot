"""
ShadBot Project Intelligence

Archive Service
"""

from __future__ import annotations

from datetime import datetime, timezone

from projectintelligence.application.archive.ports.archive_repository import (
    ArchiveRepository,
)
from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)
from projectintelligence.domain.archive.archive_entry import (
    ArchiveEntry,
)


class ArchiveService:
    """
    Application service responsible for
    creating and storing intelligence archives.
    """

    def __init__(
        self,
        repository: ArchiveRepository,
    ) -> None:
        self.repository = repository

    def archive(
        self,
        result: RuntimeResult,
        location: str,
        version: int = 1,
    ) -> ArchiveEntry:
        """
        Create archive metadata from runtime result.
        """

        entry = ArchiveEntry(
            project_id=result.pipeline_result.snapshot.project_id,
            snapshot_id=result.pipeline_result.snapshot.snapshot_id,
            version=version,
            location=location,
            created_at=datetime.now(
                timezone.utc,
            ),
        )

        self.repository.save(
            entry,
        )

        return entry

    def get_latest(
        self,
    ) -> ArchiveEntry | None:
        """
        Retrieve latest archive.
        """

        return self.repository.get_latest()
