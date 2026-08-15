"""
ShadBot Project Intelligence

Git Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class GitDifferenceService:
    """
    Compares Git metadata between snapshots.
    """

    def compare(
        self,
        previous_commit: str | None,
        current_commit: str | None,
        previous_branch: str | None,
        current_branch: str | None,
        difference: SnapshotDifference,
    ) -> None:

        difference.git_changed = (
            previous_commit != current_commit or previous_branch != current_branch
        )
