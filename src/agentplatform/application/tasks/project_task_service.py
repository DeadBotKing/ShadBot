"""
ShadBot Agent Platform

Project task service.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.application.tasks.task_loader import (
    TaskLoader,
)
from agentplatform.application.tasks.task_selector import (
    SelectableTask,
)


class ProjectTaskService:
    """
    Provides project task loading.
    """

    def __init__(
        self,
        loader: TaskLoader,
    ) -> None:
        self._loader = loader

    def get_tasks(
        self,
        project_path: Path,
    ) -> list[SelectableTask]:
        """
        Load project tasks.
        """

        return self._loader.load(
            project_path,
        )
