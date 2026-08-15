"""
ShadBot Agent Platform

Reasoning execution modes.
"""

from __future__ import annotations

from enum import Enum


class ReasoningMode(str, Enum):
    """
    Supported reasoning modes.
    """

    ANALYTICAL = "analytical"

    CREATIVE = "creative"

    DIAGNOSTIC = "diagnostic"

    PLANNING = "planning"

    IMPLEMENTATION = "implementation"

    REVIEW = "review"
