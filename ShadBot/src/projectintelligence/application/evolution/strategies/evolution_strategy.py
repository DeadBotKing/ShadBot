"""
ShadBot Project Intelligence

Evolution Strategy Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from projectintelligence.domain.evolution.evolution_change import (
    EvolutionChange,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class EvolutionStrategy(ABC):
    """
    Contract for project evolution analysis strategies.
    """

    @abstractmethod
    def analyze(
        self,
        previous: ProjectSnapshot,
        current: ProjectSnapshot,
    ) -> tuple[EvolutionChange, ...]:
        """
        Analyze one aspect of project evolution.
        """
        raise NotImplementedError
