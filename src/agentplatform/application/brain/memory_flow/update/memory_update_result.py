"""
ShadBot Agent Platform

Memory Update Result
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class MemoryUpdateResult:
    """
    Result of memory update operation.
    """

    memory_id: UUID

    updated: bool

    message: str
