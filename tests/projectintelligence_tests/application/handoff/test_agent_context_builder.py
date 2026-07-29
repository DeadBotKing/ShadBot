"""
ShadBot Project Intelligence

Agent Context Builder Tests
"""

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from projectintelligence.application.handoff.agent_context_builder import (
    AgentContextBuilder,
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
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)
from projectintelligence.domain.resume.project_state import (
    ProjectState,
)
from projectintelligence.domain.resume.project_summary import (
    ProjectSummary,
)
from projectintelligence.domain.resume.resume_metadata import (
    ResumeMetadata,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
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

    builder = AgentContextBuilder()

    previous_snapshot = ProjectSnapshot(
        project_id=snapshot.project_id,
        workspace=Path("test-project"),
    )

    evolution = ProjectEvolution(
        project_id=snapshot.project_id,
        previous_snapshot_id=previous_snapshot.snapshot_id,
        current_snapshot_id=snapshot.snapshot_id,
        changes=(
            EvolutionChange(
                path="src/main.py",
                change_type=EvolutionType.MODIFIED,
                category="source",
                description="Updated main application flow",
            ),
            EvolutionChange(
                path="src/new_module.py",
                change_type=EvolutionType.ADDED,
                category="source",
                description="Added new module",
            ),
        ),
    )

    result = builder.build(
        knowledge=knowledge,
        context=context,
        resume=resume,
        git_context=None,
        evolution=evolution,
    )

    assert result is not None
    assert "Python" in result.technologies
    assert "Django" in result.frameworks
    assert result.evolution is not None
    assert "src/new_module.py" in result.evolution.added_files
    assert "src/main.py" in result.evolution.modified_files
    assert len(result.evolution.recent_changes) == 2
