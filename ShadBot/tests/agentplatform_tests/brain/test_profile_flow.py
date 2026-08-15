"""
ShadBot Agent Platform

Unit tests for 5.7 Profile Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.profile_flow import (
    BehaviorConstraints,
    CapabilityAwareness,
    ProfileFlowService,
    ProfileLoader,
)
from agentplatform.domain.agents import AgentRole


def test_profile_loader_loads_role_style() -> None:
    loader = ProfileLoader()
    prof = loader.load(AgentRole.ARCHITECT)
    assert prof.role == AgentRole.ARCHITECT
    assert "system_architect" in prof.cognitive_style
    assert "architecture" in prof.focus_areas


def test_capability_awareness_checks_task_match() -> None:
    prof = ProfileLoader().load(AgentRole.ARCHITECT)
    res = CapabilityAwareness().check(prof, "design architecture")
    assert res.capable is True
    assert "architecture" in res.matched_focus_areas


def test_behavior_constraints_enforces_rules() -> None:
    prof = ProfileLoader().load(AgentRole.ARCHITECT)
    const = BehaviorConstraints().enforce(prof)
    assert "write_source_code" in const.forbidden_actions
    assert "design_clean_architecture" in const.mandatory_guidelines


def test_profile_flow_service_applies_complete_profile() -> None:
    service = ProfileFlowService()
    pkg = service.apply(AgentRole.ENGINEER, "implementation")
    assert pkg.profile.role == AgentRole.ENGINEER
    assert pkg.awareness.capable is True
    assert "write_production_code" in pkg.constraints.mandatory_guidelines
