"""
ShadBot Project Intelligence

Project Evolution Analyzer
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.evolution.contracts.evolution_analyzer import (
    EvolutionAnalyzer,
)
from projectintelligence.application.evolution.strategies.evolution_strategy import (
    EvolutionStrategy,
)
from projectintelligence.domain.evolution.evolution_change import (
    EvolutionChange,
)
from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class ProjectEvolutionAnalyzer(
    EvolutionAnalyzer,
):
    """
    Coordinates evolution analysis strategies.
    """

    strategies: tuple[EvolutionStrategy, ...]

    def analyze(
        self,
        previous: ProjectSnapshot,
        current: ProjectSnapshot,
    ) -> ProjectEvolution:

        changes: list[EvolutionChange] = []

        for strategy in self.strategies:
            changes.extend(
                strategy.analyze(
                    previous,
                    current,
                ),
            )

        return ProjectEvolution(
            project_id=current.project_id,
            previous_snapshot_id=previous.snapshot_id,
            current_snapshot_id=current.snapshot_id,
            changes=tuple(
                changes,
            ),
        )
