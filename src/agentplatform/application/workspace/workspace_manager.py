from agentplatform.application.workspace.workspace_registry import (
    WorkspaceRegistry,
)


class WorkspaceManager:
    def __init__(self, registry: WorkspaceRegistry) -> None:
        self._registry = registry

    def activate(self, name: str) -> None:
        workspace = self._registry.get(name)

        if workspace is None:
            raise ValueError(f"Workspace not found: {name}")

        workspace.activate()

    def deactivate(self, name: str) -> None:
        workspace = self._registry.get(name)

        if workspace is None:
            raise ValueError(f"Workspace not found: {name}")

        workspace.deactivate()
