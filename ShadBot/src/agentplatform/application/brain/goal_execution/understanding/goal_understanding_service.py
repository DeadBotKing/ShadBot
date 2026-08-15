"""
ShadBot Agent Platform

Goal Understanding Service
"""

from __future__ import annotations

from agentplatform.application.brain.goal_execution.intake import (
    Goal,
)

from .goal_analysis import (
    GoalAnalysis,
)
from .goal_understanding_result import (
    GoalUnderstandingResult,
)


class GoalUnderstandingService:
    """
    Understands execution goals.
    """

    def understand(
        self,
        goal: Goal,
    ) -> GoalUnderstandingResult:
        """
        Analyze incoming goal.
        """

        requirements = (
            requirement.strip()
            for requirement in goal.description.split("\n")
            if requirement.strip()
        )

        analysis = GoalAnalysis(
            goal_id=goal.goal_id,
            intent=goal.title,
            scope=goal.description,
            requirements=tuple(
                requirements,
            ),
        )

        return GoalUnderstandingResult(
            goal_id=goal.goal_id,
            understood=True,
            analysis=analysis,
            message="Goal understood successfully",
        )
