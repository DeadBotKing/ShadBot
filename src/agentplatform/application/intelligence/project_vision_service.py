"""
ShadBot Agent Platform

Project vision application service.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.intelligence import (
    ProjectVision,
)
from agentplatform.infrastructure.intelligence import (
    ProjectVisionRepository,
)


class ProjectVisionService:
    """
    Application service for project vision lifecycle.

    Responsible for:
    - Saving project vision
    - Loading existing vision
    - Providing shared vision context
    """

    def __init__(
        self,
        repository: ProjectVisionRepository,
    ) -> None:

        self._repository = repository

    def save(
        self,
        project_path: Path,
        vision: ProjectVision,
    ) -> None:
        """
        Persist project vision.
        """

        self._repository.save(
            project_path,
            vision,
        )

    def load(
        self,
        project_path: Path,
    ) -> dict[str, object]:
        """
        Retrieve project vision.
        """

        return self._repository.load(
            project_path,
        )

    def exists(
        self,
        project_path: Path,
    ) -> bool:
        """
        Check if project has vision.
        """

        return self._repository.exists(
            project_path,
        )

    def build_brain_context(
        self,
        project_path: Path,
    ) -> dict[str, object]:
        """
        Create shared context for all agent brains.
        """

        vision = self.load(
            project_path,
        )

        if not vision:
            return {
                "project_vision": None,
            }

        return {
            "project_vision": vision,
            "vision_source": str(
                project_path / ".shadbot" / "intelligence" / "project_vision.json"
            ),
        }
