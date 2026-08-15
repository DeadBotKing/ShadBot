"""
ShadBot Agent Platform

Goal Intake Request
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .goal_source import GoalSource


@dataclass(frozen=True, slots=True)
class GoalRequest:
    """
    Incoming goal request.
    """

    project_id: UUID

    title: str

    description: str

    source: GoalSource
