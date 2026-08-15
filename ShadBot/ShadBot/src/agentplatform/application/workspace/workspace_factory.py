"""
ShadBot Agent Platform

Workspace factory.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.workspace import (
    Project,
    Workspace,
)


class WorkspaceFactory:
    """
    Creates configured workspaces.
    """

    def create(
        self,
        name: str,
        root_path: Path,
        projects: tuple[Project, ...],
    ) -> Workspace:
        return Workspace(
            name=name,
            root_path=root_path,
            projects=projects,
        )
