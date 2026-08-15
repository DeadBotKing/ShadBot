"""
ShadBot Agent Platform

Prioritized Context
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from agentplatform.application.brain.context_assembly.collector import (
    ContextItem,
)


@dataclass(frozen=True, slots=True)
class PrioritizedContext:
    """
    Context after prioritization.
    """

    goal_id: UUID

    ordered_items: tuple[ContextItem, ...]

    highest_priority: int

    total_items: int
