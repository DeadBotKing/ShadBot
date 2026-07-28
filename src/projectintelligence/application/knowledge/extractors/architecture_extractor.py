"""
ShadBot Project Intelligence

Architecture Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class ArchitectureExtractor:
    """
    Extracts architecture knowledge from a project snapshot.
    """

    def extract(
        self,
        snapshot: ProjectSnapshot,
    ) -> tuple[str | None, list[str]]:
        """
        Extract architecture description and patterns.
        """

        description = (
            f"Project contains {snapshot.file_count} files "
            f"across {snapshot.directory_count} directories."
        )

        patterns = sorted(snapshot.architecture_tree.keys())

        return (
            description,
            patterns,
        )