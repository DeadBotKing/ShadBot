"""
ShadBot Project Intelligence

Resume Generator Test
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from projectintelligence.application.resume.completion_analyzer import (
    CompletionAnalyzer,
)
from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.resume.pending_task_analyzer import (
    PendingTaskAnalyzer,
)
from projectintelligence.application.resume.project_state_analyzer import (
    ProjectStateAnalyzer,
)
from projectintelligence.application.resume.project_summary_builder import (
    ProjectSummaryBuilder,
)
from projectintelligence.application.resume.recommendation_engine import (
    RecommendationEngine,
)
from projectintelligence.application.resume.resume_generator import (
    ResumeGenerator,
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
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_resume_generator_creates_project_resume() -> None:
    project_id = uuid4()

    snapshot = ProjectSnapshot(
        project_id=project_id,
        workspace=Path("."),
    )

    snapshot.detected_languages = [
        "Python",
    ]

    snapshot.detected_frameworks = [
        "Django",
    ]

    snapshot.dependencies = {
        "django": "5",
    }

    knowledge = ProjectKnowledge(
        project_id=project_id,
        dependency_map={
            "django": "5",
        },
    )

    context = ProjectContext(
        project_id=project_id,
        snapshot_id=snapshot.snapshot_id,
    )

    build_context = ResumeBuildContext(
        snapshot=snapshot,
        knowledge=knowledge,
        history=SnapshotHistory(
            history_id=uuid4(),
            project_id=project_id,
            created_at=datetime.now(timezone.utc),
        ),
        context=context,
    )

    generator = ResumeGenerator(
        summary_builder=ProjectSummaryBuilder(),
        completion_analyzer=CompletionAnalyzer(),
        pending_task_analyzer=PendingTaskAnalyzer(),
        recommendation_engine=RecommendationEngine(),
        project_state_analyzer=ProjectStateAnalyzer(),
    )

    resume = generator.generate(
        build_context,
    )

    assert resume.project_id == project_id
    assert resume.metadata.snapshot_id == snapshot.snapshot_id

    assert resume.state is not None
    assert resume.summary is not None

    assert isinstance(
        resume.completed_work,
        tuple,
    )

    assert isinstance(
        resume.pending_work,
        tuple,
    )

    assert isinstance(
        resume.recommendations,
        tuple,
    )
