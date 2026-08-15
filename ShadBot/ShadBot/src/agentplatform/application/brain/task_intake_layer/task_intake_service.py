"""
ShadBot Agent Platform

Unified service for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from pathlib import Path
from .task_completion_reporter import TaskCompletionReport, TaskCompletionReporter
from .task_discovery import TaskDiscovery
from .task_normalizer import NormalizedTaskPackage, TaskNormalizer
from .task_parser import TaskParser
from .task_reader import TaskReader
from .task_state_manager import TaskStateManager


class TaskIntakeService:
    """
    Orchestrates discovery, reading, parsing, normalizing, state management, and reporting for tasks/task.md.
    """

    def __init__(
        self,
        discovery: TaskDiscovery | None = None,
        reader: TaskReader | None = None,
        parser: TaskParser | None = None,
        normalizer: TaskNormalizer | None = None,
        state_mgr: TaskStateManager | None = None,
        reporter: TaskCompletionReporter | None = None,
    ) -> None:
        self._discovery = discovery or TaskDiscovery()
        self._reader = reader or TaskReader()
        self._parser = parser or TaskParser()
        self._normalizer = normalizer or TaskNormalizer()
        self._state_mgr = state_mgr or TaskStateManager()
        self._reporter = reporter or TaskCompletionReporter()

    def intake_from_workspace(self, project_path: Path) -> NormalizedTaskPackage:
        task_file = self._discovery.discover_task_file(project_path)
        if task_file is None:
            raise FileNotFoundError(f"No task.md discovered in workspace: {project_path}")

        raw_md = self._reader.read_task(task_file)
        parsed = self._parser.parse(raw_md)
        norm = self._normalizer.normalize(parsed)
        self._state_mgr.set_status(norm.task_id, "INGESTED")
        return norm

    def report_completion(self, task_id, success: bool, summary: str) -> TaskCompletionReport:
        self._state_mgr.set_status(task_id, "COMPLETED" if success else "FAILED")
        return self._reporter.report(task_id, success, summary)
