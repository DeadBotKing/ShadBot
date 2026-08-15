"""
ShadBot Project Intelligence

Technology Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class TechnologyExtractor:
    """
    Extracts technology information from a project snapshot.
    """

    def extract(
        self,
        snapshot: ProjectSnapshot,
    ) -> tuple[list[str], list[str], list[str]]:
        """
        Extract technologies, frameworks and languages.
        """

        languages = sorted(
            set(snapshot.detected_languages),
        )

        frameworks = sorted(
            set(snapshot.detected_frameworks),
        )

        technologies = sorted(
            set(languages + frameworks + list(snapshot.dependencies.keys())),
        )

        return (
            technologies,
            frameworks,
            languages,
        )
