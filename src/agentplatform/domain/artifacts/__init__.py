"""
ShadBot Agent Platform

Artifact domain models.
"""

from .artifact_repository import (
    ArtifactRepository,
)
from .artifact_status import (
    ArtifactStatus,
)
from .artifact_type import (
    ArtifactType,
)
from .generated_artifact import (
    GeneratedArtifact,
)

__all__ = [
    "ArtifactRepository",
    "ArtifactStatus",
    "ArtifactType",
    "GeneratedArtifact",
]
