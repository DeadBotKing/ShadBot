"""
ShadBot Agent Platform

Goal Completion Status
"""

from __future__ import annotations

from enum import Enum


class CompletionStatus(str, Enum):
    """
    Completion evaluation result.
    """

    COMPLETED = "completed"

    IN_PROGRESS = "in_progress"

    BLOCKED = "blocked"

    FAILED = "failed"
