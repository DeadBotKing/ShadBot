"""
ShadBot Agent Platform

Environment Understanding Result
"""

from __future__ import annotations

from dataclasses import dataclass

from .environment_profile import (
    EnvironmentProfile,
)


@dataclass(frozen=True, slots=True)
class EnvironmentUnderstandingResult:
    """
    Result of environment analysis.
    """

    profile: EnvironmentProfile

    detected: bool

    confidence: float
