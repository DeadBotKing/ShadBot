"""
ShadBot Project Intelligence

Context JSON Mapper
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from typing import Any
from uuid import UUID

from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.git.git_repository_state import (
    GitRepositoryState,
)


class ContextJsonMapper:
    """
    Maps ProjectContext objects to JSON dictionaries
    and reconstructs them back into domain objects.
    """

    @staticmethod
    def to_dict(
        context: ProjectContext,
    ) -> dict[str, Any]:

        data = asdict(context)

        data["context_id"] = str(context.context_id)
        data["project_id"] = str(context.project_id)
        data["snapshot_id"] = str(context.snapshot_id)

        return data

    @staticmethod
    def from_dict(
        data: dict[str, Any],
    ) -> ProjectContext:

        git_state = None

        if data["git_state"] is not None:
            git_state = GitRepositoryState(**data["git_state"])

        return ProjectContext(
            project_id=UUID(data["project_id"]),
            snapshot_id=UUID(data["snapshot_id"]),
            context_id=UUID(data["context_id"]),
            version=data["version"],
            created_at=datetime.fromisoformat(data["created_at"]),
            summary=data["summary"],
            architecture_context=data["architecture_context"],
            technology_context=data["technology_context"],
            dependency_context=data["dependency_context"],
            change_context=data["change_context"],
            constraint_context=data["constraint_context"],
            agent_instructions=data["agent_instructions"],
            reasoning_metadata=data["reasoning_metadata"],
            git_state=git_state,
        )
