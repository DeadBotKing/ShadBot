"""
ShadBot Agent Platform

Context Priority
"""

from __future__ import annotations

from enum import IntEnum


class ContextPriority(IntEnum):
    """
    Standard brain context priorities.
    """

    CRITICAL = 100

    HIGH = 75

    NORMAL = 50

    LOW = 25

    BACKGROUND = 0
