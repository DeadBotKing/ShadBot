"""
ShadBot Agent Platform

Artifact application service.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.artifacts import (
    GeneratedArtifact,
)
from agentplatform.infrastructure.generation import (
    FileArtifactWriter,
)


class ArtifactService:
    """
    Handles artifact persistence.
    """

    def __init__(
        self,
        writer: FileArtifactWriter | None = None,
    ) -> None:
        self._writer = writer or FileArtifactWriter()

    def save(
        self,
        artifact: GeneratedArtifact,
    ) -> Path:
        """
        Save generated artifact.
        """

        return self._writer.write(
            artifact,
        )
