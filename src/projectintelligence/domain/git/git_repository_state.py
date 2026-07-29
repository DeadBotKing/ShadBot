"""
ShadBot Project Intelligence

Git Repository State Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(slots=True)
class GitRepositoryState:
    """
    Enterprise Git repository state model.
    """

    project_id: UUID

    repository_id: UUID = field(default_factory=uuid4)

    repository_path: str = ""

    branch_name: str = ""

    current_commit: str = ""

    previous_commit: str | None = None

    commit_history: list[str] = field(default_factory=list)

    changed_files: list[str] = field(default_factory=list)

    added_files: list[str] = field(default_factory=list)

    deleted_files: list[str] = field(default_factory=list)

    modified_files: list[str] = field(default_factory=list)

    is_clean: bool = True

    last_checked_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    metadata: dict[str, object] = field(default_factory=dict)
