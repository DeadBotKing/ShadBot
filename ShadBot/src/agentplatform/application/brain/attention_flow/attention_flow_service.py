"""
ShadBot Agent Platform

Unified service for 5.13 Attention Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence
from .context_filtering import ContextFilter, FilteredContextPackage
from .focus_management import FocusArea, FocusManager
from .priority_allocation import AttentionAllocation, PriorityAllocator
from .resource_attention import ResourceAttentionManager, ResourceLimitSet


@dataclass(frozen=True, slots=True)
class CompleteAttentionPackage:
    focus_areas: tuple[FocusArea, ...]
    filtered_context: FilteredContextPackage
    allocations: tuple[AttentionAllocation, ...]
    resource_limits: ResourceLimitSet


class AttentionFlowService:
    """
    Orchestrates focus management, context filtering, priority allocation, and resource attention.
    """

    def __init__(
        self,
        focus_mgr: FocusManager | None = None,
        filter_mgr: ContextFilter | None = None,
        allocator: PriorityAllocator | None = None,
        resource_mgr: ResourceAttentionManager | None = None,
    ) -> None:
        self._focus_mgr = focus_mgr or FocusManager()
        self._filter_mgr = filter_mgr or ContextFilter()
        self._allocator = allocator or PriorityAllocator()
        self._resource_mgr = resource_mgr or ResourceAttentionManager()

    def attend(self, keywords: Sequence[str], raw_context: Mapping[str, Any]) -> CompleteAttentionPackage:
        areas = self._focus_mgr.manage_focus(keywords)
        filtered = self._filter_mgr.filter_context(raw_context, areas)
        alloc = self._allocator.allocate(areas)
        primary_topic = areas[0].topic if areas else "General"
        limits = self._resource_mgr.set_limits(primary_topic)
        return CompleteAttentionPackage(
            focus_areas=areas,
            filtered_context=filtered,
            allocations=alloc,
            resource_limits=limits,
        )
