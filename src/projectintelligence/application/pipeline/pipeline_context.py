"""
ShadBot Project Intelligence

Pipeline Context
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class PipelineContext:
    """
    Shared execution context for the Project Intelligence Pipeline.
    """

    project: ProjectEntity
