"""
ShadBot Agent Platform

Workspace domain model.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agentplatform.domain.workspace.project import Project


@dataclass(slots=True)
class WorkspaceIdentity:
    """
    Workspace identity value object.
    """

    name: str


@dataclass(slots=True)
class Workspace:
    """
    Represents an AI agent workspace.
    """

    name: str

    root_path: Path

    projects: tuple[Project, ...]

    active: bool = False

    @property
    def identity(self) -> WorkspaceIdentity:
        """
        Return workspace identity.
        """

        return WorkspaceIdentity(
            name=self.name,
        )

    def activate(self) -> None:
        """
        Activate workspace.
        """

        self.active = True

    def deactivate(self) -> None:
        """
        Deactivate workspace.
        """

        self.active = False
