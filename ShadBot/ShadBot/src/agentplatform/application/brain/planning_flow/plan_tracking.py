"""
ShadBot Agent Platform

Plan Tracking component for 5.8 Planning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from uuid import UUID, uuid4
from .agent_assignment import AssignedStep


@dataclass(frozen=True, slots=True)
class TrackedPlan:
    plan_id: UUID
    assigned_steps: tuple[AssignedStep, ...]
    completed_steps: int
    total_steps: int
    is_completed: bool


class PlanTracker:
    """
    Tracks execution progress against an assigned plan.
    """

    def __init__(self) -> None:
        self._completed: set[int] = set()

    def create_tracked(self, assigned_steps: Sequence[AssignedStep], plan_id: UUID | None = None) -> TrackedPlan:
        return TrackedPlan(
            plan_id=plan_id or uuid4(),
            assigned_steps=tuple(assigned_steps),
            completed_steps=len(self._completed),
            total_steps=len(assigned_steps),
            is_completed=(len(self._completed) >= len(assigned_steps)),
        )

    def mark_completed(self, step_number: int) -> None:
        self._completed.add(step_number)
