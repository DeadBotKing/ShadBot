"""
ShadBot Agent Platform

Context Snapshot Store
"""

from __future__ import annotations

from uuid import UUID

from .context_snapshot import (
    ContextSnapshot,
)


class ContextSnapshotStore:
    """
    In-memory snapshot storage.
    """

    def __init__(
        self,
    ) -> None:

        self._snapshots: dict[
            UUID,
            ContextSnapshot,
        ] = {}

    def save(
        self,
        snapshot: ContextSnapshot,
    ) -> None:

        self._snapshots[snapshot.goal_id] = snapshot

    def load(
        self,
        goal_id: UUID,
    ) -> ContextSnapshot | None:

        return self._snapshots.get(
            goal_id,
        )

    def exists(
        self,
        goal_id: UUID,
    ) -> bool:

        return goal_id in self._snapshots

    def remove(
        self,
        goal_id: UUID,
    ) -> None:

        self._snapshots.pop(
            goal_id,
            None,
        )
