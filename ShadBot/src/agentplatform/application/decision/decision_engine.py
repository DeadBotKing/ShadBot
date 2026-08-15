"""
ShadBot Agent Platform

Execution decision engine.
"""

from __future__ import annotations

from collections.abc import Sequence

from agentplatform.domain.decision import (
    DecisionResult,
    DecisionStatus,
)
from agentplatform.domain.results import AgentResult


class DecisionEngine:
    """
    Evaluates pipeline results and decides next action.
    """

    def decide(
        self,
        results: Sequence[AgentResult],
    ) -> DecisionResult:
        """
        Decide whether execution should finish or retry.
        """

        failed_results = [result for result in results if not result.success]

        if failed_results:
            return DecisionResult(
                status=DecisionStatus.FAILED,
                reason="One or more agents failed.",
                retry_required=False,
                metadata={
                    "failed_agents": len(failed_results),
                },
            )

        rejected_reviews = [result for result in results if result.approved is False]

        if rejected_reviews:
            return DecisionResult(
                status=DecisionStatus.RETRY,
                reason="Reviewer rejected implementation.",
                retry_required=True,
                metadata={
                    "rejected_reviews": len(rejected_reviews),
                },
            )

        return DecisionResult(
            status=DecisionStatus.ACCEPTED,
            reason="Execution completed successfully.",
            retry_required=False,
        )
