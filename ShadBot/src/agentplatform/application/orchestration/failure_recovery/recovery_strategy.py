"""
ShadBot Agent Platform

Recovery Strategy Selection component for 6.6 Failure Recovery.
"""

from __future__ import annotations

from dataclasses import dataclass
from .failure_classification import ClassifiedFailure


@dataclass(frozen=True, slots=True)
class RecoveryStrategy:
    strategy_name: str
    max_retries: int
    reroute_role: str | None


class RecoveryStrategySelector:
    """
    Selects recovery strategy based on failure classification.
    """

    def select_strategy(self, classified: ClassifiedFailure) -> RecoveryStrategy:
        if not classified.recoverable:
            return RecoveryStrategy("ABORT_EXECUTION", 0, None)
        if classified.category == "TRANSIENT_NETWORK":
            return RecoveryStrategy("RETRY_SAME_AGENT", 3, None)
        return RecoveryStrategy("REROUTE_TO_ARCHITECT", 1, "architect")
