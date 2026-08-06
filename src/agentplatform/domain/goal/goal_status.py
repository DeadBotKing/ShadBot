"""
ShadBot Agent Platform

Goal lifecycle status.
"""

from __future__ import annotations

from enum import Enum


class GoalStatus(str, Enum):
    """
    Goal execution lifecycle.
    """

    CREATED = "created"

    ANALYZING = "analyzing"

    UNDERSTOOD = "understood"

    PLANNED = "planned"

    EXECUTING = "executing"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"
