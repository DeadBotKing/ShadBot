from dataclasses import dataclass

from agentplatform.domain.workspace.workspace_identity import (
    WorkspaceIdentity,
)


@dataclass
class Workspace:
    identity: WorkspaceIdentity
    active: bool = True

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False
