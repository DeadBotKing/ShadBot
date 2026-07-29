"""
ShadBot Project Intelligence

File Evolution Strategy
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.evolution.strategies.evolution_strategy import (
    EvolutionStrategy,
)
from projectintelligence.domain.evolution.evolution_change import (
    EvolutionChange,
)
from projectintelligence.domain.evolution.evolution_type import (
    EvolutionType,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class FileEvolutionStrategy(
    EvolutionStrategy,
):
    """
    Detects file-level evolution.
    """

    def analyze(
        self,
        previous: ProjectSnapshot,
        current: ProjectSnapshot,
    ) -> tuple[EvolutionChange, ...]:

        previous_files = set(
            previous.file_hashes,
        )

        current_files = set(
            current.file_hashes,
        )

        changes: list[EvolutionChange] = []

        #
        # Added files
        #

        for path in sorted(
            current_files - previous_files,
        ):
            changes.append(
                EvolutionChange(
                    path=path,
                    change_type=EvolutionType.ADDED,
                    category="file",
                    description="File added",
                ),
            )

        #
        # Removed files
        #

        for path in sorted(
            previous_files - current_files,
        ):
            changes.append(
                EvolutionChange(
                    path=path,
                    change_type=EvolutionType.REMOVED,
                    category="file",
                    description="File removed",
                ),
            )

        #
        # Modified files
        #

        for path in sorted(
            previous_files & current_files,
        ):
            if previous.file_hashes[path] != current.file_hashes[path]:
                changes.append(
                    EvolutionChange(
                        path=path,
                        change_type=EvolutionType.MODIFIED,
                        category="file",
                        description="File modified",
                    ),
                )

        return tuple(
            changes,
        )
