"""
ShadBot Agent Platform

Architecture plan model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.architecture.architecture_directory import (
    ArchitectureDirectory,
)
from agentplatform.domain.architecture.architecture_file import (
    ArchitectureFile,
)


@dataclass(frozen=True, slots=True)
class ArchitecturePlan:
    """
    Represents a complete project architecture plan.
    """

    project_name: str

    directories: tuple[ArchitectureDirectory, ...] = field(
        default_factory=tuple,
    )

    files: tuple[ArchitectureFile, ...] = field(
        default_factory=tuple,
    )

    dependencies: tuple[str, ...] = field(
        default_factory=tuple,
    )
