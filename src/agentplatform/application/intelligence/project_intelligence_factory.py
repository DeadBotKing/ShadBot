"""
ShadBot Agent Platform

Project intelligence factory.
"""

from __future__ import annotations

from agentplatform.infrastructure.intelligence import (
    EvolutionRepository,
    ProjectVisionRepository,
)

from .evolution_service import EvolutionService
from .project_intelligence_lifecycle import (
    ProjectIntelligenceLifecycle,
)
from .project_vision_builder import (
    ProjectVisionBuilder,
)
from .project_vision_service import (
    ProjectVisionService,
)


class ProjectIntelligenceFactory:
    """
    Creates complete project intelligence pipeline.

    Dependency chain:

    Repository
        |
        v
    VisionService
        |
        v
    Lifecycle
    """

    def create(
        self,
    ) -> ProjectIntelligenceLifecycle:
        """
        Create configured lifecycle.
        """

        evolution_service = EvolutionService()

        evolution_repository = EvolutionRepository()

        repository = ProjectVisionRepository()

        service = ProjectVisionService(
            repository=repository,
        )

        builder = ProjectVisionBuilder()

        return ProjectIntelligenceLifecycle(
            vision_builder=builder,
            vision_service=service,
            evolution_service=evolution_service,
            evolution_repository=evolution_repository,
        )
