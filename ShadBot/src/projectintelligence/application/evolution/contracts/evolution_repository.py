"""
ShadBot Project Intelligence

Evolution Repository Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)


class EvolutionRepository(ABC):
    """
    Repository contract for project evolution persistence.
    """

    @abstractmethod
    def save(
        self,
        evolution: ProjectEvolution,
    ) -> None:
        """
        Save project evolution.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectEvolution | None:
        """
        Get latest evolution for project.
        """
        raise NotImplementedError
