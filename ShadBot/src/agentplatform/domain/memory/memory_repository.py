"""
ShadBot Agent Platform

Memory repository contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from .memory_record import MemoryRecord


class MemoryRepository(ABC):
    """
    Contract for project memory persistence.
    """

    @abstractmethod
    def save(
        self,
        record: MemoryRecord,
    ) -> MemoryRecord:
        raise NotImplementedError

    @abstractmethod
    def get_project_memory(
        self,
        project_id: UUID,
    ) -> list[MemoryRecord]:
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        project_id: UUID,
        query: str,
    ) -> list[MemoryRecord]:
        raise NotImplementedError

    @abstractmethod
    def delete(
        self,
        memory_id: UUID,
    ) -> None:
        raise NotImplementedError
