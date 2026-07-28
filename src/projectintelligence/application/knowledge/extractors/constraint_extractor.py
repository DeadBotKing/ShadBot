"""
ShadBot Project Intelligence

Constraint Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class ConstraintExtractor:
    """
    Extracts known project constraints.
    """

    def extract(
        self,
        snapshot: ProjectSnapshot,
    ) -> list[str]:
        """
        Extract known project constraints.
        """

        constraints: list[str] = []

        if snapshot.test_status is None:
            constraints.append("Project test status is unavailable.")

        if snapshot.quality_issues:
            constraints.append(
                "Project contains unresolved quality issues.",
            )

        if not snapshot.git_commit:
            constraints.append(
                "Snapshot is not associated with a Git commit.",
            )

        return constraints