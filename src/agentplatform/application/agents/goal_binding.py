"""
ShadBot Agent Platform

Agent Goal & Intent Binding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class GoalBinding:
    """
    Goal and intent capability attached to an agent.
    """

    goal_provider: Any

    def current_goal(
        self,
    ) -> Any:
        """
        Retrieve current goal.
        """

        return self.goal_provider.get_goal()

    def current_intent(
        self,
    ) -> Any:
        """
        Retrieve current intent.
        """

        return self.goal_provider.get_intent()
