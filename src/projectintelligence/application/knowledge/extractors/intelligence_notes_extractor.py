"""
ShadBot Project Intelligence

Intelligence Notes Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class IntelligenceNotesExtractor:
    """
    Extracts intelligence notes from project analysis.
    """

    def extract(
        self,
        snapshot: ProjectSnapshot,
    ) -> list[str]:
        """
        Extract intelligence notes.
        """

        notes: list[str] = []

        notes.append(
            f"Workspace contains {snapshot.file_count} files."
        )

        notes.append(
            f"Detected {len(snapshot.detected_languages)} programming language(s)."
        )

        notes.append(
            f"Detected {len(snapshot.detected_frameworks)} framework(s)."
        )

        notes.append(
            f"Detected {len(snapshot.dependencies)} dependency(s)."
        )

        if snapshot.quality_issues:
            notes.append(
                f"{len(snapshot.quality_issues)} quality issue(s) detected."
            )

        return notes