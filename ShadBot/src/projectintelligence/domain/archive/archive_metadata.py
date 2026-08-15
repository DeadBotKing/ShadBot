"""
ShadBot Project Intelligence

Archive Metadata Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ArchiveMetadata:
    """
    Metadata describing an archive collection
    for a project.
    """

    project_id: UUID

    total_archives: int

    latest_archive_id: UUID | None

    created_at: datetime

    updated_at: datetime
