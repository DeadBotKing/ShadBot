"""
ShadBot Agent Platform

Memory Update Request
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from agentplatform.domain.memory import MemoryRecord


@dataclass(frozen=True, slots=True)
class MemoryUpdateRequest:
    """
    Request for updating brain memory.
    """

    goal_id: UUID

    memory: MemoryRecord

    reason: str
