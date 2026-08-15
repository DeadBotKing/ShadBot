"""
ShadBot Agent Platform

Learning result.
"""

from __future__ import annotations

from dataclasses import dataclass

from .learning_status import LearningStatus


@dataclass(frozen=True, slots=True)
class LearningResult:
    """
    Result of one learning cycle.
    """

    status: LearningStatus

    learned_items: tuple[str, ...]

    confidence: float

    summary: str
