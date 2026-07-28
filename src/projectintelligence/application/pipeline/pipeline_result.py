"""
ShadBot Project Intelligence

Pipeline Result
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


@dataclass(slots=True)
class PipelineResult:
    """
    Complete result produced by the Project Intelligence Pipeline.
    """

    snapshot: ProjectSnapshot

    knowledge: ProjectKnowledge

    history: SnapshotHistory

    state: ProjectIntelligenceState

    context: ProjectContext

    git_context: GitContext | None = None

    resume: ProjectResume | None = None
    
    success: bool = True
