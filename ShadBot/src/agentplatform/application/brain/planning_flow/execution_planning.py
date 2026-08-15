"""
ShadBot Agent Platform

Execution Planning component for 5.8 Planning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .task_decomposition import SubTask


@dataclass(frozen=True, slots=True)
class PlannedStep:
    step_number: int
    subtask: SubTask
    depends_on: tuple[int, ...]


class ExecutionPlanner:
    """
    Orders subtasks into an execution schedule with dependencies.
    """

    def plan(self, subtasks: Sequence[SubTask]) -> tuple[PlannedStep, ...]:
        steps: list[PlannedStep] = []
        for idx, st in enumerate(subtasks, start=1):
            deps = (idx - 1,) if idx > 1 else ()
            steps.append(
                PlannedStep(
                    step_number=idx,
                    subtask=st,
                    depends_on=deps,
                )
            )
        return tuple(steps)
