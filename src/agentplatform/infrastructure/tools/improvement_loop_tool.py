"""
ShadBot Agent Platform

ML improvement loop tool.
"""

from __future__ import annotations

from agentplatform.domain.experiments import (
    ImprovementCycle,
)


class ImprovementLoopTool:
    """
    Controls ML improvement decisions.
    """

    def execute(
        self,
        model_name: str,
        iteration: int,
        previous_score: float,
        current_score: float,
    ) -> ImprovementCycle:
        """
        Evaluate improvement result.
        """

        improved = current_score > previous_score

        decision = "accept_new_model" if improved else "continue_experiment"

        return ImprovementCycle(
            model_name=model_name,
            iteration=iteration,
            evaluation_score=current_score,
            previous_score=previous_score,
            improved=improved,
            decision=decision,
        )
