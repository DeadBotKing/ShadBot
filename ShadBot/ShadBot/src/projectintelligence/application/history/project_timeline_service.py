"""
ShadBot Project Intelligence

Project Timeline Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)


@dataclass(slots=True)
class ProjectTimelineService:
    """
    Builds a chronological project timeline.
    """

    def build(
        self,
        history: SnapshotHistory,
    ) -> list[dict[str, object]]:

        timeline: list[dict[str, object]] = []

        for index, difference in enumerate(
            history.differences,
            start=1,
        ):
            timeline.append(
                {
                    "revision": index,
                    "changes": difference.total_changes,
                    "difference": difference,
                },
            )

        return timeline
