"""
ShadBot Agent Platform

Generated artifact domain model.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .artifact_type import ArtifactType


@dataclass(frozen=True, slots=True)
class GeneratedArtifact:
    """
    Represents generated project artifact.
    """

    path: Path

    content: str

    artifact_type: ArtifactType
