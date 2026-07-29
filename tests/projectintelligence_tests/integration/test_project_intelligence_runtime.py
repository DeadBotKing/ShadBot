"""
ShadBot Project Intelligence

Project Intelligence Runtime Integration Test
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock

from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)
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
from projectintelligence.application.handoff.agent_context_builder import (
    AgentContextBuilder,
)


def test_project_intelligence_runtime_flow() -> None:
    project = ProjectEntity(
        name="TestProject",
        workspace=Path("."),
    )

    snapshot = ProjectSnapshot(
        project_id=project.project_id,
        workspace=project.workspace,
    )

    knowledge = ProjectKnowledge(
        project_id=project.project_id,
    )

    context = ProjectContext(
        project_id=project.project_id,
        snapshot_id=snapshot.snapshot_id,
    )

    state = Mock()

    pipeline_result = PipelineResult(
        snapshot=snapshot,
        knowledge=knowledge,
        history=SnapshotHistory(),
        state=state,
        context=context,
    )

    resume = Mock()

    pipeline = Mock()

    pipeline.run.return_value = pipeline_result

    resume_generator = Mock()

    resume_generator.generate.return_value = resume

    persistence_service = Mock()

    snapshot_history_service = Mock()

    orchestrator = ProjectIntelligenceOrchestrator(
        pipeline=pipeline,
        persistence_service=persistence_service,
        snapshot_history_service=snapshot_history_service,
        resume_generator=resume_generator,
        agent_context_builder=AgentContextBuilder(),
    )

    result = orchestrator.execute(
        project,
    )

    assert isinstance(
        result,
        RuntimeResult,
    )

    assert result.pipeline_result is pipeline_result

    assert result.pipeline_result.resume is resume

    pipeline.run.assert_called_once_with(
        project,
    )

    resume_generator.generate.assert_called_once()

    persistence_service.save_all.assert_called_once_with(
        snapshot=snapshot,
        knowledge=knowledge,
        history=pipeline_result.history,
        state=state,
        context=context,
        resume=resume,
    )