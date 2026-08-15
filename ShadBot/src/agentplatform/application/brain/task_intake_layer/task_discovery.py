"""
ShadBot Agent Platform

Task Discovery component for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from pathlib import Path


class TaskDiscovery:
    """
    Discovers tasks/task.md in a target project workspace.
    """

    def discover_task_file(self, project_path: Path) -> Path | None:
        candidate = project_path / "Tasks" / "task.md"
        if candidate.exists() and candidate.is_file():
            return candidate
        root_candidate = project_path / "task.md"
        if root_candidate.exists() and root_candidate.is_file():
            return root_candidate
        return None
