"""
ShadBot Agent Platform

Working memory.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID


class WorkingMemory:
    """
    Short term execution memory.

    Stores temporary context during
    one agent execution.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            dict[str, Any],
        ] = {}

    def save(
        self,
        execution_id: UUID,
        data: dict[str, Any],
    ) -> None:
        self._storage[execution_id] = data

    def get(
        self,
        execution_id: UUID,
    ) -> dict[str, Any]:
        return self._storage.get(
            execution_id,
            {},
        )

    def clear(
        self,
        execution_id: UUID,
    ) -> None:
        self._storage.pop(
            execution_id,
            None,
        )
