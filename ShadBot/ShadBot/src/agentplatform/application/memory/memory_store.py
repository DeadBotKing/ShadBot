"""
ShadBot Agent Platform

Memory store contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from agentplatform.domain.memory import MemoryEntry


class MemoryStore(ABC):
    """
    Abstract memory storage.
    """

    @abstractmethod
    def save(
        self,
        memory: MemoryEntry,
    ) -> None:
        """
        Store memory.
        """

    @abstractmethod
    def recall(
        self,
        project_id: UUID,
    ) -> list[MemoryEntry]:
        """
        Retrieve project memories.
        """
