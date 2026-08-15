"""
ShadBot Project Intelligence

Language Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class LanguageDifferenceService:
    """
    Compares detected programming languages between snapshots.
    """

    def compare(
        self,
        previous: list[str],
        current: list[str],
        difference: SnapshotDifference,
    ) -> None:

        difference.language_changes = sorted(
            set(previous).symmetric_difference(
                current,
            ),
        )
