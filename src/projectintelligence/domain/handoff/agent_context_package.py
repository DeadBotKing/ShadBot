"""
ShadBot Project Intelligence

Agent Context Package Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


@dataclass(frozen=True, slots=True)
class AgentContextPackage:
    """
    Stable knowledge package exposed to Agent Platform.

    This model is the boundary between:
    Project Intelligence Engine
    and
    Autonomous Coding Agents.

    Agents consume this package only and must not depend
    on internal Project Intelligence implementation details.
    """

    project_id: UUID

    summary: str

    technologies: tuple[str, ...] = field(
        default_factory=tuple,
    )

    frameworks: tuple[str, ...] = field(
        default_factory=tuple,
    )

    languages: tuple[str, ...] = field(
        default_factory=tuple,
    )

    dependencies: dict[str, str] = field(
        default_factory=dict,
    )

    architecture_description: str | None = None

    conventions: tuple[str, ...] = field(
        default_factory=tuple,
    )

    constraints: tuple[str, ...] = field(
        default_factory=tuple,
    )

    recommendations: tuple[str, ...] = field(
        default_factory=tuple,
    )

    current_state: str | None = None

    project_context: ProjectContext | None = None

    project_resume: ProjectResume | None = None

    git_context: GitContext | None = None