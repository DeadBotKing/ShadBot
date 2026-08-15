"""
ShadBot Project Intelligence

In Memory Evolution Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.evolution.contracts.evolution_repository import (
    EvolutionRepository,
)
from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)


class InMemoryEvolutionRepository(
    EvolutionRepository,
):
    """
    In-memory implementation of project evolution persistence.
    """

    def __init__(self) -> None:
        self._items: list[ProjectEvolution] = []

    def save(
        self,
        evolution: ProjectEvolution,
    ) -> None:
        """
        Save project evolution.
        """

        self._items.append(
            evolution,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectEvolution | None:
        """
        Get latest evolution for project.
        """

        matches = [item for item in self._items if item.project_id == project_id]

        if not matches:
            return None

        return matches[-1]
