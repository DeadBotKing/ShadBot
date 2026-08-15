"""
ShadBot Agent Platform

Merged Context Model
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from agentplatform.application.brain.context_assembly.collector import (
    ContextItem,
)


@dataclass(frozen=True, slots=True)
class MergedContext:
    """
    Final assembled brain context.
    """

    goal_id: UUID

    items: tuple[ContextItem, ...]

    sources: tuple[str, ...]

    total_items: int
