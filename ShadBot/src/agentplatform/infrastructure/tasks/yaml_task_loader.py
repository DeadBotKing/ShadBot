"""
ShadBot Agent Platform

YAML task loader implementation.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from agentplatform.application.tasks import (
    SelectableTask,
    TaskLoader,
)


class YamlTaskLoader(TaskLoader):
    """
    Loads backlog.yaml files.
    """

    def load(
        self,
        project_path: Path,
    ) -> list[SelectableTask]:
        """
        Read project backlog tasks.
        """

        task_file = project_path / "tasks" / "backlog.yaml"

        if not task_file.exists():
            return []

        with task_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file)

        if not isinstance(data, dict):
            return []

        raw_tasks = data.get(
            "tasks",
            [],
        )

        if not isinstance(raw_tasks, list):
            return []

        tasks: list[SelectableTask] = []

        for item in raw_tasks:
            if not isinstance(item, dict):
                continue

            tasks.append(
                SelectableTask(
                    id=str(item.get("id", "")),
                    phase=str(item.get("phase", "")),
                    title=str(item.get("title", "")),
                    description=str(item.get("description", "")),
                    task_type=str(item.get("type", "")),
                    priority=str(item.get("priority", "low")),
                    status=str(item.get("status", "pending")),
                )
            )

        return tasks
