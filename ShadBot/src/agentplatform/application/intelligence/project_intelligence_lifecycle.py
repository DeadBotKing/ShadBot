"""
ShadBot Agent Platform

Project intelligence lifecycle orchestration.
"""

from __future__ import annotations

from pathlib import Path
from uuid import UUID

from agentplatform.domain.intelligence import (
    ProjectVision,
)
from agentplatform.infrastructure.intelligence import (
    EvolutionRepository,
)

from .evolution_service import (
    EvolutionService,
)
from .project_vision_builder import (
    ProjectVisionBuilder,
)
from .project_vision_service import (
    ProjectVisionService,
)


class ProjectIntelligenceLifecycle:
    """
    Controls complete project intelligence lifecycle.

    Lifecycle:

    Load
        |
    Initialize
        |
    Refresh
        |
    Finalize
    """

    def __init__(
        self,
        vision_builder: ProjectVisionBuilder,
        vision_service: ProjectVisionService,
        evolution_service: EvolutionService,
        evolution_repository: EvolutionRepository,
    ) -> None:

        self._vision_builder = vision_builder
        self._vision_service = vision_service
        self._evolution_service = evolution_service
        self._evolution_repository = evolution_repository

    def load(
        self,
        project_path: Path,
    ) -> dict[str, object]:
        """
        Load existing project vision.
        """

        return self._vision_service.load(
            project_path,
        )

    def initialize(
        self,
        project_id: UUID,
        project_path: Path,
        intelligence_data: dict[str, object],
    ) -> ProjectVision:
        """
        First project intelligence execution.

        If previous vision exists,
        lifecycle continues with refresh.
        """

        if self._vision_service.exists(
            project_path,
        ):
            return self.refresh(
                project_id,
                project_path,
                intelligence_data,
            )

        vision = self._build(
            project_id,
            project_path,
            intelligence_data,
        )

        self._vision_service.save(
            project_path,
            vision,
        )

        return vision

    def refresh(
        self,
        project_id: UUID,
        project_path: Path,
        intelligence_data: dict[str, object],
    ) -> ProjectVision:
        """
        Update project vision during lifecycle.
        """

        previous = self._vision_service.load(
            project_path,
        )

        current = self._build(
            project_id,
            project_path,
            intelligence_data,
        )

        evolution = self._evolution_service.compare(
            project_id,
            previous,
            intelligence_data,
        )

        self._evolution_repository.append(
            project_path,
            evolution,
        )

        self._vision_service.save(
            project_path,
            current,
        )

        return current

    def finalize(
        self,
        project_id: UUID,
        project_path: Path,
        intelligence_data: dict[str, object],
    ) -> ProjectVision:
        """
        Final project intelligence pass.

        Called after agents finish execution.
        """

        vision = self._build(
            project_id,
            project_path,
            intelligence_data,
        )

        self._vision_service.save(
            project_path,
            vision,
        )

        return vision

    def build_context(
        self,
        project_path: Path,
    ) -> dict[str, object]:
        """
        Build shared brain context.
        """

        return self._vision_service.build_brain_context(
            project_path,
        )

    def _build(
        self,
        project_id: UUID,
        project_path: Path,
        intelligence_data: dict[str, object],
    ) -> ProjectVision:
        """
        Build project vision object.
        """

        return self._vision_builder.build(
            project_id=project_id,
            project_path=str(
                project_path,
            ),
            data=intelligence_data,
        )
