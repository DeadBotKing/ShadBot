"""
ShadBot Project Intelligence

In Memory Evolution Repository Tests
"""

from __future__ import annotations

from uuid import uuid4

from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_evolution_repository import (
    InMemoryEvolutionRepository,
)


def create_evolution(
    project_id,
) -> ProjectEvolution:
    return ProjectEvolution(
        project_id=project_id,
        previous_snapshot_id=uuid4(),
        current_snapshot_id=uuid4(),
        changes=[],
    )


def test_in_memory_evolution_repository_stores_evolution():
    repository = InMemoryEvolutionRepository()

    project_id = uuid4()

    evolution = create_evolution(
        project_id,
    )

    repository.save(
        evolution,
    )

    latest = repository.get_latest(
        project_id,
    )

    assert latest == evolution


def test_in_memory_evolution_repository_returns_latest_evolution():
    repository = InMemoryEvolutionRepository()

    project_id = uuid4()

    first = create_evolution(
        project_id,
    )

    second = create_evolution(
        project_id,
    )

    repository.save(
        first,
    )

    repository.save(
        second,
    )

    latest = repository.get_latest(
        project_id,
    )

    assert latest == second
