"""
ShadBot Agent Platform

Context Prioritizer
"""

from __future__ import annotations

from agentplatform.application.brain.context_assembly.merger import (
    MergedContext,
)

from .prioritized_context import (
    PrioritizedContext,
)


class ContextPrioritizer:
    """
    Orders context according to execution priority.
    """

    def prioritize(
        self,
        merged_context: MergedContext,
    ) -> PrioritizedContext:
        """
        Sort context by priority.
        """

        ordered = tuple(
            sorted(
                merged_context.items,
                key=lambda item: (
                    item.priority,
                    item.created_at,
                ),
                reverse=True,
            )
        )

        highest = ordered[0].priority if ordered else 0

        return PrioritizedContext(
            goal_id=merged_context.goal_id,
            ordered_items=ordered,
            highest_priority=highest,
            total_items=len(
                ordered,
            ),
        )
