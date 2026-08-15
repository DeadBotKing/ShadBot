"""
ShadBot Agent Platform

Self improvement status.
"""

from __future__ import annotations

from enum import Enum


class ImprovementStatus(str, Enum):
    """
    Improvement lifecycle status.
    """

    REQUESTED = "requested"

    ANALYZING = "analyzing"

    APPROVED = "approved"

    REJECTED = "rejected"

    APPLIED = "applied"

    FAILED = "failed"
