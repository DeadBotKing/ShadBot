"""
ShadBot Agent Platform

Reflection types.
"""

from __future__ import annotations

from enum import Enum


class ReflectionType(str, Enum):
    """
    Reflection analysis categories.
    """

    EXECUTION = "execution"

    FAILURE = "failure"

    PERFORMANCE = "performance"

    QUALITY = "quality"

    LEARNING = "learning"
