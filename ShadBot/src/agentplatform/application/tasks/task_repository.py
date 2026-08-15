"""
ShadBot Agent Platform

Project task repository.
"""

from __future__ import annotations

from pathlib import Path
from shutil import move


class ProjectTaskRepository:
    """
    Handles project task files.
    """

    def __init__(
        self,
        tasks_directory_name: str = "tasks",
    ) -> None:
        self._tasks_directory_name = tasks_directory_name

    def get_tasks_directory(
        self,
        project_path: Path,
    ) -> Path:
        """
        Return project tasks directory.
        """

        return project_path / self._tasks_directory_name

    def get_active_task_file(
        self,
        project_path: Path,
    ) -> Path:
        """
        Return active task file path.
        """

        return self.get_tasks_directory(project_path) / "active_task.yaml"

    def get_completed_directory(
        self,
        project_path: Path,
    ) -> Path:
        """
        Return completed tasks directory.
        """

        return self.get_tasks_directory(project_path) / "completed"

    def get_failed_directory(
        self,
        project_path: Path,
    ) -> Path:
        """
        Return failed tasks directory.
        """

        return self.get_tasks_directory(project_path) / "failed"

    def archive_completed(
        self,
        project_path: Path,
    ) -> None:
        """
        Move active task to completed.
        """

        self._archive(
            self.get_active_task_file(project_path),
            self.get_completed_directory(project_path),
        )

    def archive_failed(
        self,
        project_path: Path,
    ) -> None:
        """
        Move active task to failed.
        """

        self._archive(
            self.get_active_task_file(project_path),
            self.get_failed_directory(project_path),
        )

    def _archive(
        self,
        source: Path,
        destination_directory: Path,
    ) -> None:
        """
        Move task file.
        """

        if not source.exists():
            return

        destination_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        move(
            str(source),
            str(destination_directory / source.name),
        )
