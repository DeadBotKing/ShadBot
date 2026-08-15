"""
ShadBot Agent Platform

Project memory factory.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.application.memory import (
    MemoryService,
)

from .json_memory_repository import (
    JsonMemoryRepository,
)


class ProjectMemoryFactory:
    """
    Creates isolated memory services
    per project.
    """

    @staticmethod
    def create(
        project_root: Path,
    ) -> MemoryService:

        repository = JsonMemoryRepository(
            project_root,
        )

        return MemoryService(
            repository,
        )
