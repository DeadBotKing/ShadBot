"""
ShadBot Agent Platform

Memory Query
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class MemoryQuery:
    """
    Brain memory retrieval query.
    """

    goal_id: UUID

    capability: str

    keywords: tuple[str, ...]

    max_results: int = 10
