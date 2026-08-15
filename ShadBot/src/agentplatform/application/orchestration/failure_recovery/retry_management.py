"""
ShadBot Agent Platform

Retry Management component for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from .recovery_strategy import RecoveryStrategy


@dataclass(frozen=True, slots=True)
class RetryDecision:
    should_retry: bool
    attempt_number: int
    delay_seconds: float


class RetryManager:
    """
    Manages retry attempt budgets and backoff delay.
    """

    def manage_retry(self, strategy: RecoveryStrategy, current_attempt: int) -> RetryDecision:
        should = (current_attempt <= strategy.max_retries) and (strategy.max_retries > 0)
        delay = 1.0 * current_attempt if should else 0.0
        return RetryDecision(should_retry=should, attempt_number=current_attempt, delay_seconds=delay)
