"""
ShadBot Agent Platform

Task Routing Strategy component for 6.1 Task Routing.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from .capability_analyzer import RequiredCapabilitySet
from .task_classifier import TaskClassification


class RoutingStrategy:
    """
    Selects primary and candidate agent roles based on task classification and capabilities.
    """

    def select_route(
        self,
        classification: TaskClassification,
        capabilities: RequiredCapabilitySet,
    ) -> tuple[AgentRole, tuple[AgentRole, ...], str]:
        if classification.category == "architecture":
            return (AgentRole.ARCHITECT, (AgentRole.ARCHITECT, AgentRole.RESEARCHER), "ARCHITECTURE_FIRST")
        if classification.category == "research":
            return (AgentRole.RESEARCHER, (AgentRole.RESEARCHER, AgentRole.ARCHITECT), "RESEARCH_FIRST")
        if classification.category == "review":
            return (AgentRole.REVIEWER, (AgentRole.REVIEWER, AgentRole.QA), "QUALITY_FIRST")
        return (AgentRole.ENGINEER, (AgentRole.ENGINEER, AgentRole.REVIEWER), "ENGINEERING_DIRECT")
