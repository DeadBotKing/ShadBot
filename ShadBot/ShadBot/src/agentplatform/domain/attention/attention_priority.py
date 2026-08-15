"""
ShadBot Agent Platform

Attention priority model.
"""

from __future__ import annotations

from enum import IntEnum


class AttentionPriority(IntEnum):
    """
    Context importance levels.
    """

    LOW = 1

    NORMAL = 2

    HIGH = 3

    CRITICAL = 4
