"""
ShadBot Agent Platform

Task Capability Analyzer component for 6.1 Task Routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.tasks import AgentTask
from .task_classifier import TaskClassification


@dataclass(frozen=True, slots=True)
class RequiredCapabilitySet:
    primary_capability: str
    supporting_capabilities: tuple[str, ...]


class TaskCapabilityAnalyzer:
    """
    Determines capabilities required for a classified task.
    """

    def analyze(self, task: AgentTask, classification: TaskClassification) -> RequiredCapabilitySet:
        if classification.category == "architecture":
            return RequiredCapabilitySet("architecture_design", ("system_analysis", "technology_selection"))
        if classification.category == "research":
            return RequiredCapabilitySet("technical_research", ("feasibility_analysis",))
        if classification.category == "review":
            return RequiredCapabilitySet("code_review", ("security_analysis", "quality_validation"))
        return RequiredCapabilitySet("code_generation", ("refactoring", "test_generation"))
