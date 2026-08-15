"""
ShadBot Agent Platform

Retry engine.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.retry.retry_policy import (
    RetryPolicy,
)
from agentplatform.domain.retry import RetryState


@dataclass(slots=True)
class RetryEngine:
    """
    Controls retry decisions.
    """

    policy: RetryPolicy

    def can_retry(
        self,
        retry_count: int,
    ) -> bool:
        """
        Determine whether another attempt is allowed.
        """

        return self.policy.evaluate(retry_count) == RetryState.AVAILABLE

    def remaining_attempts(
        self,
        retry_count: int,
    ) -> int:
        """
        Calculate remaining retries.
        """

        remaining = self.policy.max_retries - retry_count

        return max(
            remaining,
            0,
        )
