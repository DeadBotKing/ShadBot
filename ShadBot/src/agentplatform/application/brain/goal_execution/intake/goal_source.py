"""
ShadBot Agent Platform

Goal Source Definition
"""

from __future__ import annotations

from enum import Enum


class GoalSource(str, Enum):
    """
    Origin of goal creation.
    """

    WORKSPACE_TASK = "workspace_task"

    USER_INPUT = "user_input"

    SYSTEM_GENERATED = "system_generated"
