"""
ShadBot Agent Platform

Task Completion Reporter component for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class TaskCompletionReport:
    task_id: UUID
    completed: bool
    final_status: str
    report_summary: str


class TaskCompletionReporter:
    """
    Generates completion reports for ingested tasks.
    """

    def report(self, task_id: UUID, success: bool, summary: str) -> TaskCompletionReport:
        status = "COMPLETED" if success else "FAILED"
        return TaskCompletionReport(
            task_id=task_id,
            completed=success,
            final_status=status,
            report_summary=summary,
        )
