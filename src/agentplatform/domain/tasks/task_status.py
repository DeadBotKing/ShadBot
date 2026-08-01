"""
ShadBot Agent Platform

Task lifecycle status.
"""

from __future__ import annotations

from enum import Enum


class TaskStatus(str, Enum):
    """
    Lifecycle states of an agent task.
    """

    CREATED = "created"

    ASSIGNED = "assigned"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"
