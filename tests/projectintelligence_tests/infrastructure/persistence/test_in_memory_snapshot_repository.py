"""
ShadBot Project Intelligence

In Memory Snapshot Repository Test
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_snapshot_repository import (
    InMemorySnapshotRepository,
)


def test_in_memory_snapshot_repository_stores_snapshot() -> None:

    repository = InMemorySnapshotRepository()

    snapshot = ProjectSnapshot(
        project_id=None,
        workspace=Path("."),
    )

    repository.save(
        snapshot,
    )

    result = repository.get_by_id(
        snapshot.snapshot_id,
    )

    assert result is snapshot


def test_in_memory_snapshot_repository_get_latest() -> None:

    repository = InMemorySnapshotRepository()

    project_id = None

    snapshot = ProjectSnapshot(
        project_id=project_id,
        workspace=Path("."),
    )

    repository.save(
        snapshot,
    )

    result = repository.get_latest(
        project_id,
    )

    assert result is snapshot