"""
ShadBot Project Intelligence

Evolution Analyzer Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class EvolutionAnalyzer(ABC):
    """
    Contract for project evolution analysis.
    """

    @abstractmethod
    def analyze(
        self,
        previous: ProjectSnapshot,
        current: ProjectSnapshot,
    ) -> ProjectEvolution:
        """
        Analyze evolution between snapshots.
        """
        raise NotImplementedError
