"""
ShadBot Agent Platform

Goal Lifecycle State
"""

from __future__ import annotations

from enum import Enum


class GoalLifecycleState(str, Enum):
    """
    Goal execution lifecycle states.
    """

    CREATED = "created"

    UNDERSTANDING = "understanding"

    PLANNING = "planning"

    EXECUTING = "executing"

    VALIDATING = "validating"

    COMPLETED = "completed"

    FAILED = "failed"
