"""
ShadBot Agent Platform

Code generation service.
"""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.generation.artifact_service import (
    ArtifactService,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.artifacts import (
    ArtifactType,
    GeneratedArtifact,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.infrastructure.tools import (
    CodeExtractor,
)


class CodeGenerationService:
    """
    Generates source code artifacts.
    """

    def __init__(
        self,
        brain: AgentBrain,
        extractor: CodeExtractor | None = None,
        artifact_service: ArtifactService | None = None,
    ) -> None:
        self._brain = brain
        self._extractor = extractor or CodeExtractor()
        self._artifact_service = artifact_service or ArtifactService()

    def generate(
        self,
        context: AgentExecutionContext,
        file_path: Path,
        instructions: str,
    ) -> GeneratedArtifact:
        """
        Generate and persist source file.
        """

        generation_context = replace(
            context,
            instructions=instructions,
        )

        response = self._brain.think(
            AgentRole.ENGINEER,
            generation_context,
        )

        code = self._extractor.extract(
            response,
        )

        artifact = GeneratedArtifact(
            path=file_path,
            content=code,
            artifact_type=ArtifactType.SOURCE_CODE,
        )

        self._artifact_service.save(
            artifact,
        )

        return artifact
