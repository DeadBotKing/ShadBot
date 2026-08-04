"""
Agent Planner.

Creates execution plans from tasks.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.tasks import AgentTask


@dataclass(frozen=True, slots=True)
class AgentExecutionPlan:
    """
    Planned execution pipeline for a task.
    """

    task: AgentTask

    agents: list[AgentRole] = field(default_factory=list)


class AgentPlanner:
    """
    Creates agent execution pipelines.
    """

    def create_plan(
        self,
        task: AgentTask,
    ) -> AgentExecutionPlan:
        """
        Create execution plan based on task type.
        """

        task_type = task.task_type.value

        if task_type == "implementation":
            agents = [
                AgentRole.PROJECT_INTELLIGENCE,
                AgentRole.ARCHITECT,
                AgentRole.ENGINEER,
                AgentRole.REVIEWER,
            ]

        elif task_type == "model_training":
            agents = [
                AgentRole.ARCHITECT,
                AgentRole.ML_SCIENTIST,
                AgentRole.ENGINEER,
                AgentRole.REVIEWER,
            ]

        elif task_type == "review":
            agents = [
                AgentRole.REVIEWER,
            ]

        elif task_type == "research":
            agents = [
                AgentRole.RESEARCHER,
            ]

        else:
            agents = [
                AgentRole.ARCHITECT,
            ]

        return AgentExecutionPlan(
            task=task,
            agents=agents,
        )
