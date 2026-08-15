"""
ShadBot Agent Platform

Project State Model
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from pathlib import Path
from uuid import UUID


class ProjectLifecycleState(StrEnum):
    """
    High-level lifecycle state of a project.
    """

    DISCOVERED = "discovered"
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class ProjectFilesystemState(StrEnum):
    """
    Filesystem state of a project.
    """

    EMPTY = "empty"
    POPULATED = "populated"
    UNAVAILABLE = "unavailable"


class ProjectStateStatus(StrEnum):
    """
    Overall state status.
    """

    READY = "ready"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True, slots=True)
class ProjectState:
    """
    Immutable semantic snapshot of a project's current state.

    This model is intentionally read-only.

    It does not:
    - modify files,
    - execute commands,
    - mutate project state,
    - perform code analysis,
    - perform planning,
    - make execution decisions.
    """

    project_id: UUID
    project_name: str
    project_path: Path
    project_type: str
    project_version: str

    lifecycle_state: ProjectLifecycleState
    filesystem_state: ProjectFilesystemState
    status: ProjectStateStatus

    workspace_file_count: int
    workspace_directory_count: int

    operating_system: str
    languages: tuple[str, ...]
    frameworks: tuple[str, ...]
    tools: tuple[str, ...]
    runtime_versions: tuple[tuple[str, str], ...]

    observed_at: datetime

    @property
    def is_available(self) -> bool:
        """
        Return whether the project is currently available.
        """

        return self.lifecycle_state is ProjectLifecycleState.AVAILABLE

    @property
    def is_ready(self) -> bool:
        """
        Return whether the project is in a ready state.
        """

        return self.status is ProjectStateStatus.READY

    @property
    def has_files(self) -> bool:
        """
        Return whether the project contains files.
        """

        return self.workspace_file_count > 0

    @property
    def runtime_version_map(self) -> dict[str, str]:
        """
        Return runtime versions as a defensive dictionary copy.
        """

        return dict(self.runtime_versions)