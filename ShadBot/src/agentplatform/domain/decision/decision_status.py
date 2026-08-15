"""
ShadBot Agent Platform

Decision status model.
"""

from __future__ import annotations

from enum import Enum


class DecisionStatus(str, Enum):
    """
    Possible execution decisions.
    """

    ACCEPTED = "accepted"

    RETRY = "retry"

    FAILED = "failed"
