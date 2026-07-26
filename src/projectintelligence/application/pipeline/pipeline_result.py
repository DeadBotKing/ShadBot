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
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class PipelineResult:
    """
    Result of executing the Project Intelligence Pipeline.
    """

    snapshot: ProjectSnapshot

    context: ProjectContext

    git_context: GitContext | None = None

    success: bool = True
