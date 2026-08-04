"""
ShadBot Agent Platform

In-memory artifact repository.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.artifacts import (
    ArtifactRepository,
    GeneratedArtifact,
)


class InMemoryArtifactRepository(
    ArtifactRepository,
):
    """
    Stores artifacts in memory.
    """

    def __init__(self) -> None:
        self._artifacts: dict[
            UUID,
            GeneratedArtifact,
        ] = {}

    def save(
        self,
        artifact: GeneratedArtifact,
    ) -> None:
        """
        Save artifact.
        """

        self._artifacts[artifact.id] = artifact

    def get_by_id(
        self,
        artifact_id: UUID,
    ) -> GeneratedArtifact | None:
        """
        Get artifact by id.
        """

        return self._artifacts.get(
            artifact_id,
        )

    def list_all(
        self,
    ) -> list[GeneratedArtifact]:
        """
        List artifacts.
        """

        return list(
            self._artifacts.values(),
        )
