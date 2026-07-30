"""
ShadBot Project Intelligence

Project Intelligence Export Runtime Test
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
from uuid import uuid4

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.state.builders.project_state_builder import (
    ProjectStateBuilder,
)
from projectintelligence.application.state.project_state_service import (
    ProjectStateService,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)
from projectintelligence.application.export.context_serializer import (
    ContextSerializer,
)
from projectintelligence.application.export.knowledge_serializer import (
    KnowledgeSerializer,
)
from projectintelligence.application.export.project_intelligence_exporter import (
    ProjectIntelligenceExporter,
)
from projectintelligence.application.export.resume_serializer import (
    ResumeSerializer,
)
from projectintelligence.application.export.snapshot_serializer import (
    SnapshotSerializer,
)
from projectintelligence.application.export.state_serializer import (
    StateSerializer,
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


def test_project_intelligence_export_runtime(
    tmp_path: Path,
) -> None:

    project = ProjectEntity(
        name="ExportTestProject",
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

    history = SnapshotHistory(
        history_id=uuid4(),
        project_id=project.project_id,
        created_at=datetime.now(timezone.utc),
    )

    state_service = ProjectStateService(
        builder=ProjectStateBuilder(),
    )

    state = state_service.build(
        ResumeBuildContext(
            snapshot=snapshot,
            knowledge=knowledge,
            history=history,
            context=context,
        )
    )

    pipeline_result = PipelineResult(
        snapshot=snapshot,
        knowledge=knowledge,
        context=context,
        history=history,
        state=state,
    )

    exporter = ProjectIntelligenceExporter(
        snapshot_serializer=SnapshotSerializer(),
        knowledge_serializer=KnowledgeSerializer(),
        context_serializer=ContextSerializer(),
        state_serializer=StateSerializer(),
        resume_serializer=ResumeSerializer(),
    )

    output = exporter.export(
        pipeline_result,
        tmp_path / "project_intelligence.json",
    )

    assert output.exists()

    content = output.read_text(
        encoding="utf-8",
    )

    assert "snapshot" in content
    assert "knowledge" in content
    assert "context" in content