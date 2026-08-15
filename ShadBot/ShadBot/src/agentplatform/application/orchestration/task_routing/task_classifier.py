"""
ShadBot Agent Platform

Task Classifier component for 6.1 Task Routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from agentplatform.domain.tasks import AgentTask, TaskType


@dataclass(frozen=True, slots=True)
class TaskClassification:
    category: str
    complexity: str
    requires_multi_agent: bool


class TaskClassifier:
    """
    Classifies incoming tasks into architectural, engineering, review, or research categories.
    """

    def classify(self, task: AgentTask) -> TaskClassification:
        t_type = task.task_type.value.lower()
        title = task.title.lower()
        if "architecture" in title or "design" in title:
            return TaskClassification("architecture", "high", True)
        if "research" in title or t_type == "research":
            return TaskClassification("research", "medium", False)
        if "review" in title or t_type == "review":
            return TaskClassification("review", "medium", False)
        return TaskClassification("engineering", "high", True)
