"""
ShadBot Agent Platform

Memory service.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.memory import (
    MemoryEntry,
    MemoryRepository,
)


class MemoryService:
    """
    Application service for agent memory.
    """

    def __init__(
        self,
        repository: MemoryRepository,
    ) -> None:
        self._repository = repository

    def remember(
        self,
        project_id: UUID,
        content: str,
        source: str,
        confidence: float = 1.0,
    ) -> MemoryEntry:
        entry = MemoryEntry(
            project_id=project_id,
            content=content,
            source=source,
            confidence=confidence,
        )

        self._repository.save(entry)

        return entry

    def recall(
        self,
        project_id: UUID,
    ) -> list[MemoryEntry]:
        return list(
            self._repository.get_project_memory(
                project_id,
            )
        )
