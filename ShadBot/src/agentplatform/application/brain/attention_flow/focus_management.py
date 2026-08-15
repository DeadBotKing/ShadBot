"""
ShadBot Agent Platform

Focus Management component for 5.13 Attention Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class FocusArea:
    topic: str
    weight: float
    is_primary: bool


class FocusManager:
    """
    Manages active cognitive focus areas during brain cycles.
    """

    def manage_focus(self, keywords: Sequence[str]) -> tuple[FocusArea, ...]:
        areas: list[FocusArea] = []
        for idx, kw in enumerate(keywords):
            areas.append(
                FocusArea(
                    topic=kw,
                    weight=0.9 if idx == 0 else 0.5,
                    is_primary=(idx == 0),
                )
            )
        if not areas:
            areas.append(FocusArea(topic="General Execution", weight=1.0, is_primary=True))
        return tuple(areas)
