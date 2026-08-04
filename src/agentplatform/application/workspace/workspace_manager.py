from __future__ import annotations

from agentplatform.application.workspace.workspace_registry import (
    WorkspaceRegistry,
)
from agentplatform.domain.workspace import (
    Project,
    Workspace,
)


class WorkspaceManager:
    """
    Manages workspace lifecycle and project selection.
    """

    def __init__(
        self,
        registry: WorkspaceRegistry,
    ) -> None:
        self._registry = registry

    def activate(
        self,
        name: str,
    ) -> None:
        """
        Activate workspace.
        """

        workspace = self._require_workspace(
            name,
        )

        workspace.activate()

    def deactivate(
        self,
        name: str,
    ) -> None:
        """
        Deactivate workspace.
        """

        workspace = self._require_workspace(
            name,
        )

        workspace.deactivate()

    def select_project(
        self,
        workspace_name: str,
        project_name: str,
    ) -> Project:
        """
        Select target project inside workspace.
        """

        workspace = self._require_workspace(
            workspace_name,
        )

        for project in workspace.projects:
            if project.name == project_name:
                return project

        raise ValueError(
            f"Project not found: {project_name}",
        )

    def get_workspace(
        self,
        name: str,
    ) -> Workspace:
        """
        Get workspace by name.
        """

        return self._require_workspace(
            name,
        )

    def _require_workspace(
        self,
        name: str,
    ) -> Workspace:
        """
        Resolve workspace or fail.
        """

        workspace = self._registry.get(
            name,
        )

        if workspace is None:
            raise ValueError(
                f"Workspace not found: {name}",
            )

        return workspace
