"""
ShadBot Agent Platform

Execution Review component for 5.9 Reflection Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class ExecutionReviewResult:
    total_executed: int
    success_count: int
    failure_count: int
    overall_status: str


class ExecutionReviewer:
    """
    Reviews a batch of agent results to assess execution quality.
    """

    def review(self, results: Sequence[AgentResult]) -> ExecutionReviewResult:
        total = len(results)
        successes = sum(1 for r in results if r.success)
        failures = total - successes
        status = "SUCCESS" if failures == 0 else "PARTIAL" if successes > 0 else "FAILED"
        return ExecutionReviewResult(
            total_executed=total,
            success_count=successes,
            failure_count=failures,
            overall_status=status,
        )
