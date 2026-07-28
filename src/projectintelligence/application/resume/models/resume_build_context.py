"""
ShadBot Project Intelligence

Resume Build Context
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.context.project_context import ProjectContext
from projectintelligence.domain.history.snapshot_history import SnapshotHistory
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(frozen=True, slots=True)
class ResumeBuildContext:
    """
    Complete input required to build a project resume.

    This object acts as the application contract between the
    Project Intelligence pipeline and the Resume Engine.

    Every analyzer and generator inside the Resume Engine
    consumes this context instead of depending directly on
    pipeline services.
    """

    snapshot: ProjectSnapshot

    knowledge: ProjectKnowledge

    history: SnapshotHistory

    context: ProjectContext