"""
ShadBot Agent Platform

Artifact domain package.
"""

from .artifact_type import ArtifactType
from .generated_artifact import GeneratedArtifact

__all__ = [
    "ArtifactType",
    "GeneratedArtifact",
]
