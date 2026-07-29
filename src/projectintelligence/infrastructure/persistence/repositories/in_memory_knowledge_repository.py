"""
ShadBot Project Intelligence

In Memory Knowledge Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.ports.outbound.knowledge_repository import (
    KnowledgeRepository,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)


class InMemoryKnowledgeRepository(
    KnowledgeRepository,
):
    """
    In-memory implementation of knowledge persistence.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            ProjectKnowledge,
        ] = {}

    def save(
        self,
        knowledge: ProjectKnowledge,
    ) -> None:
        self._storage[knowledge.knowledge_id] = knowledge

    def update(
        self,
        knowledge: ProjectKnowledge,
    ) -> None:
        self._storage[knowledge.knowledge_id] = knowledge

    def delete(
        self,
        knowledge_id: UUID,
    ) -> None:
        self._storage.pop(
            knowledge_id,
            None,
        )

    def exists(
        self,
        knowledge_id: UUID,
    ) -> bool:
        return knowledge_id in self._storage

    def get_by_id(
        self,
        knowledge_id: UUID,
    ) -> ProjectKnowledge | None:
        return self._storage.get(
            knowledge_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectKnowledge | None:

        knowledge_items = [
            knowledge
            for knowledge in self._storage.values()
            if knowledge.project_id == project_id
        ]

        if not knowledge_items:
            return None

        return max(
            knowledge_items,
            key=lambda item: item.created_at,
        )

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectKnowledge]:

        return [
            knowledge
            for knowledge in self._storage.values()
            if knowledge.project_id == project_id
        ]

    def count(
        self,
        project_id: UUID,
    ) -> int:

        return len(
            self.list_by_project(
                project_id,
            ),
        )
