"""
ShadBot Project Intelligence

Archive Service Test
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock

from projectintelligence.application.archive.archive_service import (
    ArchiveService,
)
from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.infrastructure.persistence.archive.in_memory_archive_repository import (
    InMemoryArchiveRepository,
)


def create_runtime_result() -> RuntimeResult:

    project = ProjectEntity(
        name="TestProject",
        workspace=Path("."),
    )

    snapshot = ProjectSnapshot(
        project_id=project.project_id,
        workspace=project.workspace,
    )

    context = ProjectContext(
        project_id=project.project_id,
        snapshot_id=snapshot.snapshot_id,
    )

    pipeline_result = PipelineResult(
        snapshot=snapshot,
        knowledge=ProjectKnowledge(
            project_id=project.project_id,
        ),
        history=Mock(),
        state=Mock(),
        context=context,
    )

    return RuntimeResult(
        pipeline_result=pipeline_result,
    )


def test_archive_service_creates_archive_entry() -> None:

    repository = InMemoryArchiveRepository()

    service = ArchiveService(
        repository=repository,
    )

    result = create_runtime_result()

    entry = service.archive(
        result=result,
        location="archives/intelligence_001.json",
    )

    assert entry.project_id == (result.pipeline_result.snapshot.project_id)

    assert entry.snapshot_id == (result.pipeline_result.snapshot.snapshot_id)

    stored = repository.get_by_id(
        entry.archive_id,
    )

    assert stored is entry


def test_archive_service_returns_latest_archive() -> None:

    repository = InMemoryArchiveRepository()

    service = ArchiveService(
        repository=repository,
    )

    first = service.archive(
        result=create_runtime_result(),
        location="archives/first.json",
        version=1,
    )

    second = service.archive(
        result=create_runtime_result(),
        location="archives/second.json",
        version=2,
    )

    latest = service.get_latest()

    assert latest is second
    assert latest is not first
