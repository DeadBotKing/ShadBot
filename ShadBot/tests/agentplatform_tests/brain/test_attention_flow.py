"""
ShadBot Agent Platform

Unit tests for 5.13 Attention Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.attention_flow import (
    AttentionFlowService,
    ContextFilter,
    FocusManager,
    PriorityAllocator,
    ResourceAttentionManager,
)


def test_focus_manager_creates_focus_areas() -> None:
    areas = FocusManager().manage_focus(["architecture", "security"])
    assert len(areas) == 2
    assert areas[0].is_primary is True


def test_context_filter_reduces_context() -> None:
    raw = {"architecture_plan": "Layered", "debug_logs": "trace", "instructions": "build"}
    areas = FocusManager().manage_focus(["architecture"])
    pkg = ContextFilter().filter_context(raw, areas)
    assert "architecture_plan" in pkg.retained_keys
    assert "instructions" in pkg.retained_keys
    assert pkg.reduction_ratio >= 0.0


def test_priority_allocator_distributes_budget() -> None:
    areas = FocusManager().manage_focus(["architecture", "security"])
    alloc = PriorityAllocator().allocate(areas)
    assert sum(a.attention_budget_percent for a in alloc) >= 99


def test_resource_attention_manager_sets_limits() -> None:
    lim_arch = ResourceAttentionManager().set_limits("architecture")
    assert lim_arch.max_tokens == 8192
    assert lim_arch.allow_deep_reasoning is True


def test_attention_flow_service_orchestrates_attention() -> None:
    service = AttentionFlowService()
    pkg = service.attend(["architecture"], {"architecture": "ok", "irrelevant": "no"})
    assert len(pkg.focus_areas) == 1
    assert "architecture" in pkg.filtered_context.retained_keys
