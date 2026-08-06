"""
ShadBot Agent Platform

Agent experience memory.
"""

from __future__ import annotations

from dataclasses import dataclass

from .memory_record import MemoryRecord


@dataclass(frozen=True, slots=True)
class ExperienceRecord:
    """
    Agent execution experience.
    """

    memory: MemoryRecord

    task: str

    action: list[str]

    result: dict[str, object]

    score: float
