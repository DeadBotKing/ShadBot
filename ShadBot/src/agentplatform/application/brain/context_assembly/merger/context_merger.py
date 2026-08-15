"""
ShadBot Agent Platform

Context Merger
"""

from __future__ import annotations

from agentplatform.application.brain.context_assembly.collector import (
    ContextCollection,
)

from .context_merge_strategy import (
    ContextMergeStrategy,
)
from .merged_context import (
    MergedContext,
)


class ContextMerger:
    """
    Combines multiple context items into one brain context.
    """

    def merge(
        self,
        *,
        collection: ContextCollection,
        strategy: ContextMergeStrategy = (ContextMergeStrategy.PRIORITY_BASED),
    ) -> MergedContext:
        """
        Merge collected contexts.
        """

        items = collection.items

        if strategy == ContextMergeStrategy.PRIORITY_BASED:
            items = tuple(
                sorted(
                    items,
                    key=lambda item: item.priority,
                    reverse=True,
                )
            )

        sources = tuple(sorted({item.source.value for item in items}))

        return MergedContext(
            goal_id=collection.goal_id,
            items=items,
            sources=sources,
            total_items=len(items),
        )
