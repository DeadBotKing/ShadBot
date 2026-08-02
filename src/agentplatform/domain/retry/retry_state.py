"""
ShadBot Agent Platform

Retry state model.
"""

from __future__ import annotations

from enum import Enum


class RetryState(str, Enum):
    """
    Retry lifecycle states.
    """

    AVAILABLE = "available"

    EXHAUSTED = "exhausted"
