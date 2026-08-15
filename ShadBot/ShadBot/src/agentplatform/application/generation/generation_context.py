"""
ShadBot Agent Platform

Generation context.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.artifacts import ArtifactType


@dataclass(frozen=True, slots=True)
class GenerationContext:
    """
    Context required for artifact generation.
    """

    file_path: str

    artifact_type: ArtifactType

    instructions: str
