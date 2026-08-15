"""
ShadBot Agent Platform

Task Decomposition component for 5.8 Planning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class SubTask:
    subtask_id: UUID
    title: str
    description: str
    required_role: str


class TaskDecomposer:
    """
    Decomposes large project tasks into manageable subtasks.
    """

    def decompose(self, task_title: str, task_description: str) -> tuple[SubTask, ...]:
        return (
            SubTask(
                subtask_id=uuid4(),
                title=f"Analyze & Design for {task_title}",
                description="Create architecture design and technical plan.",
                required_role="architect",
            ),
            SubTask(
                subtask_id=uuid4(),
                title=f"Implement {task_title}",
                description="Write clean implementation code following architecture.",
                required_role="engineer",
            ),
            SubTask(
                subtask_id=uuid4(),
                title=f"Review & Validate {task_title}",
                description="Review implementation and ensure quality standards.",
                required_role="reviewer",
            ),
        )
