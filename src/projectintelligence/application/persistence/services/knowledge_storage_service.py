"""
ShadBot Project Intelligence

Knowledge Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.ports.outbound.knowledge_repository import (
    KnowledgeRepository,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)


@dataclass(slots=True)
class KnowledgeStorageService:
    """
    Coordinates persistence of project knowledge.
    """

    repository: KnowledgeRepository

    def save(
        self,
        knowledge: ProjectKnowledge,
    ) -> PersistenceResult:
        self.repository.save(
            knowledge,
        )

        return PersistenceResult.succeeded(
            operation="save",
            entity="ProjectKnowledge",
            identifier=str(knowledge.knowledge_id),
            message="Project knowledge stored successfully.",
        )
