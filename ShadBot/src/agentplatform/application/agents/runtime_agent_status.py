"""
ShadBot Agent Platform

Runtime Agent Status
"""

from __future__ import annotations

from enum import Enum


class RuntimeAgentStatus(str, Enum):
    """
    Runtime lifecycle state of an agent.
    """

    IDLE = "idle"

    THINKING = "thinking"

    PLANNING = "planning"

    EXECUTING = "executing"

    WAITING = "waiting"

    VALIDATING = "validating"

    REFLECTING = "reflecting"

    LEARNING = "learning"

    COMPLETED = "completed"

    FAILED = "failed"
