"""
ShadBot Agent Platform

Priority Management component for 5.12 Goal & Intent Flow.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PriorityAllocation:
    priority_level: str
    execution_timeout_seconds: int
    max_retries: int


class PriorityManager:
    """
    Allocates execution priority and resource budgets to aligned goals.
    """

    def prioritize(self, is_aligned: bool) -> PriorityAllocation:
        if is_aligned:
            return PriorityAllocation(
                priority_level="CRITICAL",
                execution_timeout_seconds=300,
                max_retries=3,
            )
        return PriorityAllocation(
            priority_level="STANDARD",
            execution_timeout_seconds=120,
            max_retries=1,
        )
