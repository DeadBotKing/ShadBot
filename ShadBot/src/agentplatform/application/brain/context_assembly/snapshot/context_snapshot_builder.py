"""
ShadBot Agent Platform

Context Snapshot Builder
"""

from __future__ import annotations

from agentplatform.application.brain.context_assembly.prioritizer import (
    PrioritizedContext,
)

from .context_snapshot import (
    ContextSnapshot,
)


class ContextSnapshotBuilder:
    """
    Builds immutable context snapshots.
    """

    def build(
        self,
        prioritized_context: PrioritizedContext,
    ) -> ContextSnapshot:
        """
        Build snapshot.
        """

        return ContextSnapshot(
            goal_id=prioritized_context.goal_id,
            prioritized_context=prioritized_context,
        )
