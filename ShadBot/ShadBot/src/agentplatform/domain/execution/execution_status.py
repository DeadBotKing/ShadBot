"""
ShadBot Agent Platform

Execution status definitions.
"""

from __future__ import annotations

from enum import Enum


class ExecutionStatus(str, Enum):
    """
    Execution lifecycle states.
    """

    CREATED = "created"

    RUNNING = "running"

    WAITING = "waiting"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"
