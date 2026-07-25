"""
ShadBot Project Intelligence

Project Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from uuid import UUID, uuid4


@dataclass(slots=True)
class ProjectEntity:
    """
    Enterprise project representation.

    Represents a software project managed by
    Project Intelligence Engine.
    """

    name: str

    workspace: Path

    project_id: UUID = field(
        default_factory=uuid4
    )

    description: str | None = None

    repository_path: Path | None = None

    languages: list[str] = field(
        default_factory=list
    )

    frameworks: list[str] = field(
        default_factory=list
    )

    platforms: list[str] = field(
        default_factory=list
    )

    environment: str | None = None

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = field(
        default_factory=datetime.utcnow
    )

    last_snapshot_id: UUID | None = None

    knowledge_version: str = "1.0"

    analysis_status: str = "created"