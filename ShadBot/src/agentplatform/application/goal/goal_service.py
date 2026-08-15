"""
ShadBot Agent Platform

Goal application service.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.goal import Goal

from .goal_analyzer import GoalAnalyzer


class GoalService:
    """
    Application service for goal lifecycle.
    """

    def __init__(
        self,
        analyzer: GoalAnalyzer | None = None,
    ) -> None:

        self._analyzer = analyzer or GoalAnalyzer()

    def understand(
        self,
        project_id: UUID,
        request: str,
        context: dict[str, object] | None = None,
    ) -> Goal:
        """
        Understand raw request.
        """

        return self._analyzer.analyze(
            project_id,
            request,
            context,
        )

    def build_brain_context(
        self,
        goal: Goal,
    ) -> dict[str, object]:
        """
        Convert goal into brain input.
        """

        return {
            "goal_context": goal.to_context(),
        }
