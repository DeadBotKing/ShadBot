"""
ShadBot Agent Platform

Memory repository contract.
"""

from __future__ import annotations

from collections.abc import Sequence
from uuid import UUID

from .memory_entry import MemoryEntry


class MemoryRepository:
    """
    Memory persistence contract.
    """

    def save(
        self,
        entry: MemoryEntry,
    ) -> None:
        raise NotImplementedError

    def get_project_memory(
        self,
        project_id: UUID,
    ) -> Sequence[MemoryEntry]:
        raise NotImplementedError
