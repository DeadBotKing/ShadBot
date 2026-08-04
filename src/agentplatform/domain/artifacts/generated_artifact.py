"""
ShadBot Agent Platform

Generated artifact domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from uuid import UUID, uuid4

from .artifact_status import ArtifactStatus
from .artifact_type import ArtifactType


@dataclass(frozen=True, slots=True)
class GeneratedArtifact:
    """
    Represents generated project artifact.
    """

    path: Path

    content: str

    artifact_type: ArtifactType

    status: ArtifactStatus = ArtifactStatus.CREATED

    id: UUID = field(
        default_factory=uuid4,
    )
