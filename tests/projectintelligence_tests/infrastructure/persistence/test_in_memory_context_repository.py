"""
ShadBot Project Intelligence

In Memory Context Repository Test
"""

from __future__ import annotations

from uuid import uuid4

from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_context_repository import (
    InMemoryContextRepository,
)


def test_in_memory_context_repository_stores_context() -> None:

    repository = InMemoryContextRepository()

    context = ProjectContext(
        project_id=uuid4(),
        snapshot_id=uuid4(),
    )

    repository.save(
        context,
    )

    result = repository.get_by_id(
        context.context_id,
    )

    assert result is context


def test_in_memory_context_repository_get_by_snapshot() -> None:

    repository = InMemoryContextRepository()

    context = ProjectContext(
        project_id=uuid4(),
        snapshot_id=uuid4(),
    )

    repository.save(
        context,
    )

    result = repository.get_by_snapshot(
        context.snapshot_id,
    )

    assert result is context
