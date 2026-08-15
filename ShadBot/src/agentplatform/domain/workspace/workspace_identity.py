from dataclasses import dataclass


@dataclass(frozen=True)
class WorkspaceIdentity:
    name: str
    root_path: str
    description: str = ""
