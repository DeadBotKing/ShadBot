"""
ShadBot Project Intelligence

Context Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.ports.outbound.context_repository import (
    ContextRepository,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)


@dataclass(slots=True)
class ContextStorageService:
    """
    Application service responsible for project context persistence.
    """

    repository: ContextRepository

    def save(
        self,
        context: ProjectContext,
    ) -> PersistenceResult:
        self.repository.save(context)

        return PersistenceResult.succeeded(
            operation="save",
            entity="ProjectContext",
            identifier=str(context.context_id),
            message="Project context stored successfully.",
        )

    def update(
        self,
        context: ProjectContext,
    ) -> PersistenceResult:
        self.repository.update(context)

        return PersistenceResult.succeeded(
            operation="update",
            entity="ProjectContext",
            identifier=str(context.context_id),
            message="Project context updated successfully.",
        )

    def delete(
        self,
        context: ProjectContext,
    ) -> PersistenceResult:
        self.repository.delete(context.context_id)

        return PersistenceResult.succeeded(
            operation="delete",
            entity="ProjectContext",
            identifier=str(context.context_id),
            message="Project context deleted successfully.",
        )
