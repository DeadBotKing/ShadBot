"""
ShadBot Agent Platform

Unit tests for 6.2 Agent Selection.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.orchestration.agent_selection import (
    AgentDiscovery,
    AgentSelectionService,
    AvailabilityChecker,
    CapabilityMatcher,
    PriorityEvaluator,
)
from agentplatform.application.orchestration.task_routing import AgentRouteDecision
from agentplatform.application.registry import AgentRegistry
from agentplatform.domain.agents import AgentRole
from agentplatform.infrastructure.agents import ArchitectAgent


def test_agent_discovery_finds_registered_agent() -> None:
    reg = AgentRegistry()
    reg.register(AgentRole.ARCHITECT, ArchitectAgent(role=AgentRole.ARCHITECT))
    disc = AgentDiscovery(reg)
    found = disc.discover((AgentRole.ARCHITECT,))
    assert len(found) == 1
    assert found[0].name == "architect"


def test_capability_matcher_filters_capable() -> None:
    agent = ArchitectAgent(role=AgentRole.ARCHITECT)
    matched = CapabilityMatcher().filter_capable([agent], "architecture_design")
    assert len(matched) == 1


def test_availability_checker_returns_available() -> None:
    agent = ArchitectAgent(role=AgentRole.ARCHITECT)
    avail = AvailabilityChecker().check_available([agent])
    assert len(avail) == 1


def test_priority_evaluator_ranks_candidates() -> None:
    agent = ArchitectAgent(role=AgentRole.ARCHITECT)
    ranked = PriorityEvaluator().evaluate([agent], AgentRole.ARCHITECT)
    assert ranked[0][1] >= 0.98


def test_agent_selection_service_selects_top_agent() -> None:
    reg = AgentRegistry()
    reg.register(AgentRole.ARCHITECT, ArchitectAgent(role=AgentRole.ARCHITECT))
    service = AgentSelectionService(reg)
    route = AgentRouteDecision(
        task_id=uuid4(),
        required_role=AgentRole.ARCHITECT,
        candidate_roles=(AgentRole.ARCHITECT,),
        routing_strategy="ARCHITECTURE_FIRST",
        is_valid=True,
        validation_notes="ok",
    )
    sel = service.select_agent(route)
    assert sel.agent.name == "architect"
    assert sel.selection_score >= 0.95
