"""
ShadBot Project Intelligence

Project Context Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from projectintelligence.domain.git.git_repository_state import (
    GitRepositoryState,
)


@dataclass(slots=True)
class ProjectContext:
    """
    Enterprise runtime context provided to agents.
    """

    project_id: UUID

    snapshot_id: UUID

    context_id: UUID = field(default_factory=uuid4)

    version: str = "1.0"

    created_at: datetime = field(default_factory=datetime.utcnow)

    summary: str = ""

    architecture_context: list[str] = field(default_factory=list)

    technology_context: list[str] = field(default_factory=list)

    dependency_context: list[str] = field(default_factory=list)

    change_context: list[str] = field(default_factory=list)

    constraint_context: list[str] = field(default_factory=list)

    agent_instructions: list[str] = field(default_factory=list)

    reasoning_metadata: dict[str, object] = field(default_factory=dict)

    git_state: GitRepositoryState | None = None
