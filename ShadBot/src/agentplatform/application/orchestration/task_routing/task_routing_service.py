"""
ShadBot Agent Platform

Unified Task Routing Service for 6.1 Task Routing.
"""

from __future__ import annotations

from agentplatform.domain.tasks import AgentTask
from .agent_route_decision import AgentRouteDecision
from .capability_analyzer import TaskCapabilityAnalyzer
from .routing_strategy import RoutingStrategy
from .routing_validator import RoutingValidator
from .task_classifier import TaskClassifier


class TaskRoutingService:
    """
    Orchestrates classification, capability analysis, routing strategy, and validation.
    """

    def __init__(
        self,
        classifier: TaskClassifier | None = None,
        analyzer: TaskCapabilityAnalyzer | None = None,
        strategy: RoutingStrategy | None = None,
        validator: RoutingValidator | None = None,
    ) -> None:
        self._classifier = classifier or TaskClassifier()
        self._analyzer = analyzer or TaskCapabilityAnalyzer()
        self._strategy = strategy or RoutingStrategy()
        self._validator = validator or RoutingValidator()

    def route_task(self, task: AgentTask) -> AgentRouteDecision:
        cls_res = self._classifier.classify(task)
        caps = self._analyzer.analyze(task, cls_res)
        primary_role, candidates, strat_name = self._strategy.select_route(cls_res, caps)
        valid, notes = self._validator.validate(primary_role, candidates)
        return AgentRouteDecision(
            task_id=task.id,
            required_role=primary_role,
            candidate_roles=candidates,
            routing_strategy=strat_name,
            is_valid=valid,
            validation_notes=notes,
        )
