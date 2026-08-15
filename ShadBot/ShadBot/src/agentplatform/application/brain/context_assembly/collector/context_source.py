"""
ShadBot Agent Platform

Context Source Definition
"""

from __future__ import annotations

from enum import Enum


class ContextSource(str, Enum):
    """
    Available context providers.
    """

    GOAL = "goal"

    WORKSPACE = "workspace"

    MEMORY = "memory"

    EYE = "eye"

    PROFILE = "profile"

    EXECUTION = "execution"
