"""
ShadBot Project Intelligence

Project Snapshot Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from uuid import UUID, uuid4


@dataclass(slots=True)
class ProjectSnapshot:
    """
    Enterprise snapshot of a project state.
    """

    project_id: UUID

    workspace: Path

    snapshot_id: UUID = field(
        default_factory=uuid4
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    file_count: int = 0

    directory_count: int = 0

    file_hashes: dict[str, str] = field(
        default_factory=dict
    )

    detected_languages: list[str] = field(
        default_factory=list
    )

    detected_frameworks: list[str] = field(
        default_factory=list
    )

    dependencies: dict[str, str] = field(
        default_factory=dict
    )

    architecture_tree: dict[str, object] = field(
        default_factory=dict
    )

    git_commit: str | None = None

    git_branch: str | None = None

    changed_files: list[str] = field(
        default_factory=list
    )

    test_status: str | None = None

    quality_issues: list[str] = field(
        default_factory=list
    )