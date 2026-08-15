"""
ShadBot Agent Platform

Ranked Memory Result
"""

from __future__ import annotations

from dataclasses import dataclass

from .memory_score import MemoryScore


@dataclass(frozen=True, slots=True)
class RankedMemoryResult:
    """
    Ranked memories.
    """

    ranked_items: tuple[MemoryScore, ...]

    total_items: int
