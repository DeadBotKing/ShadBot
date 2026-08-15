"""
ShadBot Agent Platform

Agent Learning Binding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class LearningBinding:
    """
    Learning capability attached to an agent.
    """

    learning_provider: Any

    def learn(
        self,
        experience: Any,
    ) -> Any:
        """
        Submit experience to learning loop.
        """

        return self.learning_provider.learn(
            experience,
        )

    def improve(
        self,
    ) -> Any:
        """
        Request improvement insights.
        """

        return self.learning_provider.improve()
