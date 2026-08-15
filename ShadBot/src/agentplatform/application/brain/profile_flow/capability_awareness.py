"""
ShadBot Agent Platform

Capability Awareness component for 5.7 Profile Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .profile_loader import LoadedProfile


@dataclass(frozen=True, slots=True)
class CapabilityMatchResult:
    capable: bool
    confidence: float
    matched_focus_areas: tuple[str, ...]


class CapabilityAwareness:
    """
    Checks agent profile capability against task requirements.
    """

    def check(self, profile: LoadedProfile, task_type: str) -> CapabilityMatchResult:
        task_lower = task_type.lower()
        matched = tuple(f for f in profile.focus_areas if f in task_lower)
        capable = bool(matched) or ("general" in profile.cognitive_style) or (profile.role.value in task_lower)
        confidence = 0.95 if capable else 0.40
        return CapabilityMatchResult(
            capable=capable,
            confidence=confidence,
            matched_focus_areas=matched,
        )
