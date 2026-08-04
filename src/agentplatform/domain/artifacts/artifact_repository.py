"""
ShadBot Agent Platform

Artifact repository contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from .generated_artifact import GeneratedArtifact


class ArtifactRepository(ABC):
    """
    Stores generated artifacts.
    """

    @abstractmethod
    def save(
        self,
        artifact: GeneratedArtifact,
    ) -> None:
        """
        Persist artifact.
        """

    @abstractmethod
    def get_by_id(
        self,
        artifact_id: UUID,
    ) -> GeneratedArtifact | None:
        """
        Retrieve artifact by identifier.
        """

    @abstractmethod
    def list_all(
        self,
    ) -> list[GeneratedArtifact]:
        """
        List stored artifacts.
        """
