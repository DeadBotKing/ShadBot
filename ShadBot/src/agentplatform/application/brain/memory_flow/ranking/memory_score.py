"""
ShadBot Agent Platform

Memory Score
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.memory import MemoryRecord


@dataclass(frozen=True, slots=True)
class MemoryScore:
    """
    Memory relevance score.
    """

    record: MemoryRecord

    score: float
