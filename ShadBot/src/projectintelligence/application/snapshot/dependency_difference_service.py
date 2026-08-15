"""
ShadBot Project Intelligence

Dependency Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class DependencyDifferenceService:
    """
    Compares dependency manifests between snapshots.
    """

    def compare(
        self,
        previous: dict[str, str],
        current: dict[str, str],
        difference: SnapshotDifference,
    ) -> None:

        difference.added_dependencies = {
            name: version for name, version in current.items() if name not in previous
        }

        difference.removed_dependencies = {
            name: version for name, version in previous.items() if name not in current
        }

        difference.updated_dependencies = {
            name: current[name]
            for name in previous.keys() & current.keys()
            if previous[name] != current[name]
        }
