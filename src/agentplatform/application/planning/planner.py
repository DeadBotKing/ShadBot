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

        agents: list[AgentRole] = []

        if task.task_type.value in {
            "implementation",
            "model_training",
        }:
            agents = [
                AgentRole.RESEARCHER,
                AgentRole.ARCHITECT,
                AgentRole.ENGINEER,
                AgentRole.REVIEWER,
            ]

        elif task.task_type.value == "review":
            agents = [
                AgentRole.REVIEWER,
            ]

        elif task.task_type.value == "research":
            agents = [
                AgentRole.RESEARCHER,
            ]

        elif task.task_type.value == "trading_analysis":
            agents = [
                AgentRole.RESEARCHER,
                AgentRole.TRADER,
                AgentRole.REVIEWER,
            ]

        else:
            agents = [
                AgentRole.ARCHITECT,
            ]

        return AgentExecutionPlan(
            task=task,
            agents=agents,
        )
