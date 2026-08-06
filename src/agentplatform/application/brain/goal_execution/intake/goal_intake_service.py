"""
ShadBot Agent Platform

Goal Intake Service
"""

from __future__ import annotations

from .goal_entity import (
    Goal,
)
from .goal_request import (
    GoalRequest,
)


class GoalIntakeService:
    """
    Creates execution goals from incoming tasks.
    """

    def create_goal(
        self,
        request: GoalRequest,
    ) -> Goal:
        """
        Convert incoming task into goal.
        """

        return Goal(
            project_id=request.project_id,
            title=request.title,
            description=request.description,
            source=request.source.value,
        )
