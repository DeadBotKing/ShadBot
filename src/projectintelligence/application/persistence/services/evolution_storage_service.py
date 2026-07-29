"""
ShadBot Project Intelligence

Evolution Storage Service
"""

from __future__ import annotations

from projectintelligence.application.evolution.contracts.evolution_repository import (
    EvolutionRepository,
)
from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)


class EvolutionStorageService:
    """
    Handles persistence operations for project evolution.
    """

    def __init__(
        self,
        repository: EvolutionRepository,
    ) -> None:
        self.repository = repository

    def save(
        self,
        evolution: ProjectEvolution,
    ) -> PersistenceResult:
        self.repository.save(
            evolution,
        )

        return PersistenceResult(
            success=True,
        )
