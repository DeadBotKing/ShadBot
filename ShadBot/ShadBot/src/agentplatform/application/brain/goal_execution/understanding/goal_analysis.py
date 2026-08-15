"""
ShadBot Agent Platform

Goal Analysis Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class GoalAnalysis:
    """
    Represents analyzed goal information.
    """

    goal_id: UUID

    intent: str

    scope: str

    requirements: tuple[str, ...]

    risks: tuple[str, ...] = ()

    analysis_id: UUID = field(
        default_factory=uuid4,
    )
