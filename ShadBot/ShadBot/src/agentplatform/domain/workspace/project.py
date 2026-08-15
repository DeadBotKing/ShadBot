"""
ShadBot Agent Platform

Workspace project domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Project:
    """
    Enterprise project identity inside workspace.

    Represents a software/trading project
    managed by autonomous agents.
    """

    name: str

    path: Path

    project_type: str

    id: UUID = field(
        default_factory=uuid4,
    )

    description: str = ""

    version: str = "1.0.0"

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    @property
    def exists(self) -> bool:
        """
        Check project workspace availability.
        """

        return self.path.exists()

    @property
    def identifier(self) -> str:
        """
        Stable project identifier.
        """

        return str(self.id)

    def with_metadata(
        self,
        metadata: dict[str, object],
    ) -> "Project":
        """
        Create immutable project copy
        with updated metadata.
        """

        return Project(
            id=self.id,
            name=self.name,
            path=self.path,
            project_type=self.project_type,
            description=self.description,
            version=self.version,
            metadata=metadata,
        )
