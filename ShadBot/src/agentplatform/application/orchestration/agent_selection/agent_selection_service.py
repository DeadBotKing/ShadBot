"""
ShadBot Agent Platform

Unified Agent Selection Service for 6.2 Agent Selection.
"""

from __future__ import annotations

from agentplatform.application.orchestration.task_routing import AgentRouteDecision
from agentplatform.application.registry import AgentRegistry
from .agent_discovery import AgentDiscovery
from .availability_checker import AvailabilityChecker
from .capability_matcher import CapabilityMatcher
from .priority_evaluator import PriorityEvaluator
from .selected_agent import SelectedAgentPackage


class AgentSelectionService:
    """
    Orchestrates discovery, capability matching, availability, priority evaluation, and selection.
    """

    def __init__(
        self,
        registry: AgentRegistry,
        discovery: AgentDiscovery | None = None,
        matcher: CapabilityMatcher | None = None,
        checker: AvailabilityChecker | None = None,
        evaluator: PriorityEvaluator | None = None,
    ) -> None:
        self._discovery = discovery or AgentDiscovery(registry)
        self._matcher = matcher or CapabilityMatcher()
        self._checker = checker or AvailabilityChecker()
        self._evaluator = evaluator or PriorityEvaluator()

    def select_agent(self, route_decision: AgentRouteDecision) -> SelectedAgentPackage:
        candidates = self._discovery.discover(route_decision.candidate_roles)
        if not candidates:
            raise RuntimeError(f"No registered agents found for candidate roles: {route_decision.candidate_roles}")

        capable = self._matcher.filter_capable(candidates, str(route_decision.required_role.value))
        available = self._checker.check_available(capable)
        ranked = self._evaluator.evaluate(available, route_decision.required_role)
        top_agent, score = ranked[0]
        role = getattr(top_agent, "role", route_decision.required_role)

        return SelectedAgentPackage(
            agent=top_agent,
            role=role,
            selection_score=score,
            selection_reason=f"Selected {top_agent.name} (Score {score}) for {route_decision.routing_strategy}",
        )
