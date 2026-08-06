"""
ShadBot Agent Platform

Context Collector
"""

from __future__ import annotations

from uuid import UUID

from .context_collection import (
    ContextCollection,
)
from .context_item import (
    ContextItem,
)


class ContextCollector:
    """
    Collects context required by brain.
    """

    def collect(
        self,
        *,
        goal_id: UUID,
        items: tuple[ContextItem, ...],
    ) -> ContextCollection:
        """
        Build context collection.
        """

        if not items:
            raise ValueError("Context collection cannot be empty")

        return ContextCollection(
            goal_id=goal_id,
            items=items,
            total_items=len(items),
        )
