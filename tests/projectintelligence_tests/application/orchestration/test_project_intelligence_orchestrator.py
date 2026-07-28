"""
ShadBot Project Intelligence

Project Intelligence Orchestrator Test
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock
from uuid import uuid4

from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
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
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


def test_orchestrator_generates_resume() -> None:

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

    knowledge = ProjectKnowledge(
        project_id=project.project_id,
    )

    pipeline_result = PipelineResult(
        snapshot=snapshot,
        knowledge=knowledge,
        history=SnapshotHistory(),
        state=Mock(),
        context=context,
    )

    pipeline = Mock()

    pipeline.run.return_value = pipeline_result

    previous_snapshot = ProjectSnapshot(
        project_id=project.project_id,
        workspace=project.workspace,
    )

    snapshot_history_service = Mock()

    snapshot_history_service.get_latest_snapshot.return_value = (
        previous_snapshot
    )

    resume = Mock(spec=ProjectResume)

    resume_generator = Mock()

    resume_generator.generate.return_value = resume

    persistence_service = Mock()

    orchestrator = ProjectIntelligenceOrchestrator(
        pipeline=pipeline,
        persistence_service=persistence_service,
        snapshot_history_service=snapshot_history_service,
        resume_generator=resume_generator,
    )

    result = orchestrator.execute(
        project,
    )

    assert result.pipeline_result.resume is resume
    assert result.previous_snapshot is previous_snapshot

    pipeline.run.assert_called_once_with(
        project,
    )

    resume_generator.generate.assert_called_once()

    persistence_service.save_all.assert_called_once_with(
        snapshot=snapshot,
        knowledge=knowledge,
        history=pipeline_result.history,
        state=pipeline_result.state,
        context=context,
        resume=resume,
    )