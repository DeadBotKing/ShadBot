"""
ShadBot Agent Platform

Project intelligence vision model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ProjectIdentity:
    """
    Basic project identity.
    """

    project_id: UUID

    name: str

    path: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )


@dataclass(frozen=True, slots=True)
class ArchitectureState:
    """
    Current architecture understanding.
    """

    description: str

    modules: tuple[str, ...]

    patterns: tuple[str, ...]

    dependencies: dict[str, str]


@dataclass(frozen=True, slots=True)
class TechnologyState:
    """
    Technology landscape.
    """

    languages: tuple[str, ...]

    frameworks: tuple[str, ...]

    tools: tuple[str, ...]

    databases: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class DevelopmentState:
    """
    Development progress state.
    """

    completed_tasks: tuple[str, ...]

    pending_tasks: tuple[str, ...]

    active_tasks: tuple[str, ...]

    decisions: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class QualityState:
    """
    Quality information.
    """

    tests_status: str

    validation_status: str

    known_issues: tuple[str, ...]

    risks: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class RuntimeState:
    """
    Runtime intelligence.
    """

    health_status: str

    performance_notes: tuple[str, ...]

    runtime_errors: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ChangeState:
    """
    Recent project changes.
    """

    changed_files: tuple[str, ...]

    commits: tuple[str, ...]

    summary: str


@dataclass(frozen=True, slots=True)
class ProjectVision:
    """
    Complete project understanding package.

    This is the shared vision provided
    to all agent brains.
    """

    identity: ProjectIdentity

    architecture: ArchitectureState

    technologies: TechnologyState

    development: DevelopmentState

    quality: QualityState

    runtime: RuntimeState

    changes: ChangeState

    recommendations: tuple[str, ...]

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
