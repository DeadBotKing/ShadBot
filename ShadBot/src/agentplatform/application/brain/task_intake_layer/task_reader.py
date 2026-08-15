"""
ShadBot Agent Platform

Task Reader component for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from pathlib import Path


class TaskReader:
    """
    Reads markdown content from a task file.
    """

    def read_task(self, task_file: Path) -> str:
        if not task_file.exists():
            raise FileNotFoundError(f"Task file not found at: {task_file}")
        return task_file.read_text(encoding="utf-8")
