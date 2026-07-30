"""
ShadBot Project Intelligence

Archive Timeline Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from projectintelligence.domain.archive.archive_entry import (
    ArchiveEntry,
)


@dataclass(slots=True)
class ArchiveTimeline:
    """
    Represents the historical timeline of
    Project Intelligence archives.

    Timeline keeps the ordered evolution
    of project intelligence states.
    """

    project_id: UUID

    entries: list[ArchiveEntry] = field(
        default_factory=list,
    )

    @property
    def total_entries(self) -> int:
        """
        Return number of archived versions.
        """

        return len(self.entries)

    @property
    def latest_entry(self) -> ArchiveEntry | None:
        """
        Return the latest archive entry.
        """

        if not self.entries:
            return None

        return max(
            self.entries,
            key=lambda entry: entry.version,
        )
