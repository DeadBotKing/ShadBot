"""
ShadBot Agent Platform

Goal and intent context provider.
"""

from __future__ import annotations

from agentplatform.domain.goal import (
    Goal,
    Intent,
)


class GoalContextProvider:
    """
    Provides goal and intent context.
    """

    def __init__(
        self,
        goal: Goal,
        intent: Intent,
    ) -> None:

        self._goal = goal
        self._intent = intent

    def provide(
        self,
    ) -> dict[str, object]:
        """
        Build goal context.
        """

        return {
            "goal": self._goal.description,
            "intent": self._intent.name,
            "status": self._goal.status.value,
        }
