"""
ShadBot Agent Platform

File artifact writer.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.artifacts import (
    GeneratedArtifact,
)


class FileArtifactWriter:
    """
    Writes generated artifacts to filesystem.
    """

    def write(
        self,
        artifact: GeneratedArtifact,
    ) -> Path:
        """
        Persist generated artifact.
        """

        artifact.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        artifact.path.write_text(
            artifact.content,
            encoding="utf-8",
        )

        return artifact.path
