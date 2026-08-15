"""
ShadBot Agent Platform

Task loader contract.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.application.tasks.task_selector import (
    SelectableTask,
)


class TaskLoader:
    """
    Loads project tasks.
    """

    def load(
        self,
        project_path: Path,
    ) -> list[SelectableTask]:
        """
        Load selectable tasks from project.
        """

        raise NotImplementedError
