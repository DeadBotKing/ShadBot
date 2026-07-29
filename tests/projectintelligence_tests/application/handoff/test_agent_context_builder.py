"""
ShadBot Project Intelligence

Agent Context Builder Tests
"""

from uuid import uuid4
from pathlib import Path
from datetime import datetime, timezone

from projectintelligence.domain.resume.resume_metadata import (
    ResumeMetadata,
)
from projectintelligence.domain.resume.project_state import (
    ProjectState,
)
from projectintelligence.domain.resume.project_summary import (
    ProjectSummary,
)
from projectintelligence.application.handoff.agent_context_builder import (
    AgentContextBuilder,
)
from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)


def test_agent_context_builder_creates_agent_package():

    snapshot = ProjectSnapshot(
        project_id=uuid4(),
        workspace=Path("test-project"),
    )

    knowledge = ProjectKnowledge(
        project_id=snapshot.project_id,
        technologies=[
            "Python",
        ],
        frameworks=[
            "Django",
        ],
        languages=[
            "Python",
        ],
    )

    context = ProjectContext(
        project_id=snapshot.project_id,
        snapshot_id=snapshot.snapshot_id,
        version="1.0",
    )

    resume = ProjectResume(
        project_id=snapshot.project_id,
        metadata=ResumeMetadata(
            resume_id=uuid4(),
            snapshot_id=snapshot.snapshot_id,
            generated_at=datetime.now(timezone.utc),
            generator_version="1.0",
        ),
        state=ProjectState(
            current_phase="Project Intelligence Engine",
            current_sub_phase="Active",
            architecture_version="1.0",
            completed_components=1,
            pending_components=0,
            total_components=1,
            completion_percentage=100.0,
        ),
        summary=ProjectSummary(
            title="Test Project",
            overview="Test project summary",
            architecture_summary="Test architecture",
            current_focus="Testing handoff",
            latest_changes="Initial analysis",
            next_goal="Continue development",
        ),
        completed_work=(),
        pending_work=(),
        recommendations=(),
    )

    history = SnapshotHistory()

    build_context = ResumeBuildContext(
        snapshot=snapshot,
        knowledge=knowledge,
        history=history,
        context=context,
    )

    builder = AgentContextBuilder()

    result = builder.build(
        knowledge=knowledge,
        context=context,
        resume=resume,
        git_context=None,
    )

    assert result is not None
    assert "Python" in result.technologies
    assert "Django" in result.frameworks