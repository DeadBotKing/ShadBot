"""
ShadBot Agent Platform

Context Filtering component for 5.13 Attention Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping
from .focus_management import FocusArea


@dataclass(frozen=True, slots=True)
class FilteredContextPackage:
    retained_keys: tuple[str, ...]
    filtered_data: dict[str, Any]
    reduction_ratio: float


class ContextFilter:
    """
    Filters raw brain context based on active focus areas to reduce token waste.
    """

    def filter_context(
        self,
        raw_context: Mapping[str, Any],
        focus_areas: tuple[FocusArea, ...],
    ) -> FilteredContextPackage:
        retained: dict[str, Any] = {}
        primary_topics = [f.topic.lower() for f in focus_areas if f.is_primary]
        for key, val in raw_context.items():
            k_lower = key.lower()
            if any(p in k_lower for p in primary_topics) or key in ("project_id", "instructions", "task_id"):
                retained[key] = val
        if not retained and raw_context:
            retained = dict(raw_context)

        total_keys = len(raw_context)
        ret_keys = len(retained)
        ratio = round(1.0 - (ret_keys / max(1, total_keys)), 2)

        return FilteredContextPackage(
            retained_keys=tuple(retained.keys()),
            filtered_data=retained,
            reduction_ratio=max(0.0, ratio),
        )
