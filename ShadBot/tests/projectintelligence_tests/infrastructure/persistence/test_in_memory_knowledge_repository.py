"""
ShadBot Project Intelligence

In Memory Knowledge Repository Test
"""

from __future__ import annotations

from uuid import uuid4

from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_knowledge_repository import (
    InMemoryKnowledgeRepository,
)


def test_in_memory_knowledge_repository_stores_knowledge() -> None:

    repository = InMemoryKnowledgeRepository()

    knowledge = ProjectKnowledge(
        project_id=uuid4(),
    )

    repository.save(
        knowledge,
    )

    result = repository.get_by_id(
        knowledge.knowledge_id,
    )

    assert result is knowledge


def test_in_memory_knowledge_repository_get_latest() -> None:

    repository = InMemoryKnowledgeRepository()

    knowledge = ProjectKnowledge(
        project_id=uuid4(),
    )

    repository.save(
        knowledge,
    )

    result = repository.get_latest(
        knowledge.project_id,
    )

    assert result is knowledge
