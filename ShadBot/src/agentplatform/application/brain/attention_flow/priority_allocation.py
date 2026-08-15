"""
ShadBot Agent Platform

Priority Allocation component for 5.13 Attention Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .focus_management import FocusArea


@dataclass(frozen=True, slots=True)
class AttentionAllocation:
    topic: str
    attention_budget_percent: int


class PriorityAllocator:
    """
    Allocates percentage attention budgets across focus areas.
    """

    def allocate(self, focus_areas: tuple[FocusArea, ...]) -> tuple[AttentionAllocation, ...]:
        total_weight = sum(f.weight for f in focus_areas) or 1.0
        allocations: list[AttentionAllocation] = []
        for f in focus_areas:
            pct = int(round((f.weight / total_weight) * 100))
            allocations.append(
                AttentionAllocation(
                    topic=f.topic,
                    attention_budget_percent=pct,
                )
            )
        return tuple(allocations)
