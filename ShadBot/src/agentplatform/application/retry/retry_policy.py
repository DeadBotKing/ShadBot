"""
ShadBot Agent Platform

Retry policy.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.retry import RetryState


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    """
    Defines retry execution limits.
    """

    max_retries: int = 3

    def evaluate(
        self,
        retry_count: int,
    ) -> RetryState:
        """
        Check retry availability.
        """

        if retry_count >= self.max_retries:
            return RetryState.EXHAUSTED

        return RetryState.AVAILABLE
