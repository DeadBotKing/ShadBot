"""
ShadBot Agent Platform

Short term memory.
"""

from __future__ import annotations

from uuid import UUID


class ShortTermMemory:
    """
    Stores temporary execution context.
    """

    def __init__(self) -> None:
        self._storage: dict[UUID, dict[str, object]] = {}

    def remember(
        self,
        execution_id: UUID,
        key: str,
        value: object,
    ) -> None:
        """
        Store temporary data.
        """

        if execution_id not in self._storage:
            self._storage[execution_id] = {}

        self._storage[execution_id][key] = value

    def recall(
        self,
        execution_id: UUID,
    ) -> dict[str, object]:
        """
        Retrieve execution memory.
        """

        return self._storage.get(
            execution_id,
            {},
        )
