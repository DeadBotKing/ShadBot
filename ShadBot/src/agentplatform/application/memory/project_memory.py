"""
ShadBot Agent Platform

Project memory.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.memory import MemoryEntry


class ProjectMemory:
    """
    Persistent project knowledge memory.
    """

    def __init__(self) -> None:
        self._memories: dict[UUID, list[MemoryEntry]] = {}

    def remember(
        self,
        project_id: UUID,
        memory: MemoryEntry,
    ) -> None:
        """
        Store project knowledge.
        """

        if project_id not in self._memories:
            self._memories[project_id] = []

        self._memories[project_id].append(
            memory,
        )

    def recall(
        self,
        project_id: UUID,
    ) -> list[MemoryEntry]:
        """
        Retrieve project knowledge.
        """

        return self._memories.get(
            project_id,
            [],
        )
