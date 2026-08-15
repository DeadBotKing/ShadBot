"""
ShadBot Agent Platform

Context Collection
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .context_item import (
    ContextItem,
)


@dataclass(frozen=True, slots=True)
class ContextCollection:
    """
    Collected brain context.
    """

    goal_id: UUID

    items: tuple[ContextItem, ...]

    total_items: int
