"""
ShadBot Agent Platform

Memory Retrieval Result
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.memory import MemoryRecord


@dataclass(frozen=True, slots=True)
class MemoryRetrievalResult:
    """
    Retrieved memory records.
    """

    records: tuple[MemoryRecord, ...]

    total_records: int
