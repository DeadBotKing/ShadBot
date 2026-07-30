"""
ShadBot Project Intelligence

Project Intelligence Runtime Integration Test
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock
from uuid import uuid4

from projectintelligence.application.handoff.agent_context_builder import (
    AgentContextBuilder,
)
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
from projectintelligence.domain.evolution.evolution_change import (
    EvolutionChange,
)
from projectintelligence.domain.evolution.evolution_type import (
    EvolutionType,
)
from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
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
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
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
        history=SnapshotHistory(
            history_id=uuid4(),
            project_id=uuid4(),
            created_at=datetime.now(timezone.utc),
        ),
        state=state,
        context=context,
    )

    resume = Mock(spec=ProjectResume)

    resume.recommendations = ()

    pipeline = Mock()

    pipeline.run.return_value = pipeline_result

    resume_generator = Mock()

    resume_generator.generate.return_value = resume

    persistence_service = Mock()

    snapshot_history_service = Mock()

    evolution_analyzer = Mock()

    evolution = ProjectEvolution(
        project_id=project.project_id,
        previous_snapshot_id=snapshot.snapshot_id,
        current_snapshot_id=snapshot.snapshot_id,
        changes=(
            EvolutionChange(
                path="src/main.py",
                change_type=EvolutionType.MODIFIED,
                category="source",
                description="Modified application flow",
            ),
        ),
    )

    evolution_analyzer.analyze.return_value = evolution

    orchestrator = ProjectIntelligenceOrchestrator(
        pipeline=pipeline,
        persistence_service=persistence_service,
        snapshot_history_service=snapshot_history_service,
        resume_generator=resume_generator,
        agent_context_builder=AgentContextBuilder(),
        evolution_analyzer=evolution_analyzer,
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

    assert result.pipeline_result.evolution is evolution

    assert result.pipeline_result.agent_context is not None

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
        agent_context=result.pipeline_result.agent_context,
        evolution=evolution,
    )
