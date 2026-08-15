"""
ShadBot Agent Platform

Injected Memory
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.memory import MemoryRecord


@dataclass(frozen=True, slots=True)
class InjectedMemory:
    """
    Memory injected into reasoning context.
    """

    record: MemoryRecord

    score: float

    injection_order: int
