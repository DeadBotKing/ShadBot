"""
ShadBot Agent Platform

Project evolution service.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.intelligence import (
    EvolutionChange,
    ProjectEvolution,
)


class EvolutionService:
    """
    Detects project evolution.
    """

    def compare(
        self,
        project_id: UUID,
        previous: dict[str, object],
        current: dict[str, object],
    ) -> ProjectEvolution:
        """
        Compare previous and current intelligence.
        """

        changes: list[EvolutionChange] = []

        previous_files = previous.get(
            "files",
            [],
        )

        current_files = current.get(
            "files",
            [],
        )

        if previous_files != current_files:
            changes.append(
                EvolutionChange(
                    change_type="files",
                    target="workspace",
                    description="Project files changed.",
                )
            )

        if previous.get(
            "architecture",
        ) != current.get(
            "architecture",
        ):
            changes.append(
                EvolutionChange(
                    change_type="architecture",
                    target="system",
                    description="Architecture changed.",
                )
            )

        return ProjectEvolution(
            project_id=project_id,
            previous_version="previous",
            current_version="current",
            changes=tuple(
                changes,
            ),
            impact_summary=self._impact(
                changes,
            ),
        )

    def _impact(
        self,
        changes: list[EvolutionChange],
    ) -> str:
        """
        Generate impact summary.
        """

        if not changes:
            return "No significant changes detected."

        return f"{len(changes)} project evolution changes detected."
