"""
ShadBot Project Intelligence

Runtime Result
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class RuntimeResult:
    """
    Represents the result of a complete Project Intelligence
    runtime execution.
    """

    pipeline_result: PipelineResult

    previous_snapshot: ProjectSnapshot | None = None
