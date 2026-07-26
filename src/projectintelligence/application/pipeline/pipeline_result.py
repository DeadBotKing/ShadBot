"""
ShadBot Project Intelligence

Pipeline Result
"""

from __future__ import annotations

from dataclasses import dataclass

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

    success: bool = True
