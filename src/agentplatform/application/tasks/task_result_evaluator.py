"""
ShadBot Agent Platform

Task result evaluation.
"""

from __future__ import annotations

from agentplatform.domain.results import (
    AgentResult,
)


class TaskResultEvaluator:
    """
    Evaluates agent execution results.
    """

    def is_successful(
        self,
        results: list[AgentResult],
    ) -> bool:
        """
        Determine whether task execution succeeded.
        """

        return all(result.success for result in results)
