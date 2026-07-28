"""
ShadBot Project Intelligence

Convention Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class ConventionExtractor:
    """
    Extracts project conventions from a project snapshot.
    """

    def extract(
        self,
        snapshot: ProjectSnapshot,
    ) -> tuple[list[str], list[str]]:
        """
        Extract project conventions and coding rules.
        """

        conventions: list[str] = []

        coding_rules: list[str] = []

        if snapshot.detected_languages:
            conventions.append("Language-specific project conventions detected.")

        if snapshot.detected_frameworks:
            conventions.append("Framework conventions detected.")

        if snapshot.test_status is not None:
            coding_rules.append("Project includes automated testing.")

        if snapshot.quality_issues:
            coding_rules.append("Quality validation is enabled.")

        return (
            conventions,
            coding_rules,
        )
