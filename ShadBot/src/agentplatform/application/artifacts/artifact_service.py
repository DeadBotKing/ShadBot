"""
ShadBot Agent Platform

Artifact application service.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.artifacts import (
    ArtifactRepository,
    GeneratedArtifact,
)


class ArtifactService:
    """
    Application service for artifact management.
    """

    def __init__(
        self,
        repository: ArtifactRepository,
    ) -> None:
        self._repository = repository

    def register(
        self,
        artifact: GeneratedArtifact,
    ) -> GeneratedArtifact:
        """
        Register generated artifact.
        """

        self._repository.save(
            artifact,
        )

        return artifact

    def get(
        self,
        artifact_id: UUID,
    ) -> GeneratedArtifact | None:
        """
        Get artifact.
        """

        return self._repository.get_by_id(
            artifact_id,
        )

    def all(
        self,
    ) -> list[GeneratedArtifact]:
        """
        Return all artifacts.
        """

        return self._repository.list_all()
