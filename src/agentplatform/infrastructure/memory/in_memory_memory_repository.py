"""
ShadBot Agent Platform

In memory agent memory repository.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from uuid import UUID

from agentplatform.domain.memory import (
    MemoryEntry,
    MemoryRepository,
)


class InMemoryMemoryRepository(MemoryRepository):
    """
    Temporary memory storage implementation.

    Replaceable with database/vector storage.
    """

    def __init__(self) -> None:
        self._storage: dict[UUID, list[MemoryEntry]] = defaultdict(list)

    def save(
        self,
        entry: MemoryEntry,
    ) -> None:
        self._storage[entry.project_id].append(entry)

    def get_project_memory(
        self,
        project_id: UUID,
    ) -> Sequence[MemoryEntry]:
        return tuple(
            self._storage.get(
                project_id,
                [],
            )
        )
