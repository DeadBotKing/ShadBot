"""
ShadBot Project Intelligence

Archive Entry Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ArchiveEntry:
    """
    Represents a single archived Project Intelligence result.

    An archive entry is an immutable reference to one
    intelligence snapshot stored by the Archive subsystem.
    """

    project_id: UUID

    snapshot_id: UUID

    version: int

    location: str

    created_at: datetime

    archive_id: UUID = field(
        default_factory=uuid4,
    )
