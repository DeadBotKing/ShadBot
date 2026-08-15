"""
ShadBot Agent Platform

In memory agent memory repository.
"""

from __future__ import annotations

from typing import Any

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

    def search(
        self,
        project_id: UUID,
        query: str,
    ) -> Sequence[MemoryEntry]:
        results: list[MemoryEntry] = []
        for entry in self._storage.get(project_id, []):
            if query.lower() in str(getattr(entry, "content", "")).lower() or query.lower() in str(getattr(entry, "source", getattr(entry, "source_agent", ""))).lower():
                results.append(entry)
        return tuple(results)

    def delete(
        self,
        memory_id: UUID,
    ) -> bool:
        deleted = False
        for pid in list(self._storage.keys()):
            before = len(self._storage[pid])
            self._storage[pid] = [e for e in self._storage[pid] if getattr(e, "id", None) != memory_id and getattr(e, "memory_id", None) != memory_id]
            if len(self._storage[pid]) < before:
                deleted = True
        return deleted

    def update(self, entry: Any) -> Any:
        self.save(entry)
        return entry
