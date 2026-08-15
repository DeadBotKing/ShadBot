"""
ShadBot Agent Platform

Goal Progress Model
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class GoalProgress:
    """
    Represents current goal execution progress.
    """

    goal_id: UUID

    percentage: float

    current_stage: str

    completed_steps: tuple[str, ...]

    remaining_steps: tuple[str, ...]
