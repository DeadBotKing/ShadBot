from agentplatform.domain.workspace import Workspace


class WorkspaceRegistry:
    def __init__(self) -> None:
        self._workspaces: dict[str, Workspace] = {}

    def register(self, workspace: Workspace) -> None:
        self._workspaces[workspace.identity.name] = workspace

    def get(self, name: str) -> Workspace | None:
        return self._workspaces.get(name)

    def all(self) -> list[Workspace]:
        return list(self._workspaces.values())

    def count(self) -> int:
        return len(self._workspaces)
