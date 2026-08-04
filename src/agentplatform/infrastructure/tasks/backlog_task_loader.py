"""
ShadBot Agent Platform

Backlog task loader.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True, slots=True)
class BacklogTask:
    """
    Task loaded from project backlog.
    """

    id: str

    phase: str

    title: str

    task_type: str

    priority: str

    status: str


class BacklogTaskLoader:
    """
    Loads backlog.yaml files.
    """

    def load(
        self,
        project_path: Path,
    ) -> list[BacklogTask]:
        """
        Load tasks from project backlog.
        """

        backlog_file = project_path / "tasks" / "backlog.yaml"

        if not backlog_file.exists():
            return []

        with backlog_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file)

        if not isinstance(
            data,
            dict,
        ):
            return []

        raw_tasks = data.get(
            "tasks",
            [],
        )

        if not isinstance(
            raw_tasks,
            list,
        ):
            return []

        tasks: list[BacklogTask] = []

        for item in raw_tasks:
            if not isinstance(
                item,
                dict,
            ):
                continue

            tasks.append(
                BacklogTask(
                    id=str(item.get("id", "")),
                    phase=str(item.get("phase", "")),
                    title=str(item.get("title", "")),
                    task_type=str(item.get("type", "")),
                    priority=str(item.get("priority", "low")),
                    status=str(item.get("status", "pending")),
                )
            )

        return tasks
