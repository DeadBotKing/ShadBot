"""
ShadBot Agent Platform

Project memory service.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.memory import (
    MemoryRecord,
    MemoryRepository,
)


class MemoryService:
    """
    Application service for persistent project memory.
    """

    def __init__(
        self,
        repository: MemoryRepository,
    ) -> None:

        self._repository = repository

    def remember(
        self,
        record: MemoryRecord,
    ) -> MemoryRecord:
        """
        Store new project memory.
        """

        return self._repository.save(
            record,
        )

    def recall(
        self,
        project_id: UUID,
    ) -> list[MemoryRecord]:
        """
        Retrieve project memories.
        """

        return self._repository.get_project_memory(
            project_id,
        )

    def search(
        self,
        project_id: UUID,
        query: str,
    ) -> list[MemoryRecord]:
        """
        Search project knowledge.
        """

        return self._repository.search(
            project_id,
            query,
        )

    def delete(
        self,
        memory_id: UUID,
    ) -> None:
        """
        Remove memory.
        """

        self._repository.delete(
            memory_id,
        )
