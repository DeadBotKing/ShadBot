"""
ShadBot Project Intelligence

Dependency Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class DependencyExtractor:
    """
    Extracts dependency knowledge from a project snapshot.
    """

    def extract(
        self,
        snapshot: ProjectSnapshot,
    ) -> dict[str, str]:
        """
        Extract normalized dependency map.
        """

        return dict(
            sorted(
                snapshot.dependencies.items(),
                key=lambda item: item[0].lower(),
            ),
        )
