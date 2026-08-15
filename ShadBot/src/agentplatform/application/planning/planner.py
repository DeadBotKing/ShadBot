"""
ShadBot Agent Platform

Agent planning engine.
"""

from __future__ import annotations

from typing import Any

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.planning import (
    ExecutionPlan,
    PlanningRequest,
)


class AgentPlanner:
    """
    Creates execution pipelines from planning requests.
    """

    def plan(
        self,
        request: PlanningRequest,
    ) -> ExecutionPlan:
        """
        Create execution plan based on task.
        """

        task_type = request.task.task_type.value

        if task_type == "implementation":

            agents = (
                AgentRole.PROJECT_INTELLIGENCE,
                AgentRole.ARCHITECT,
                AgentRole.ENGINEER,
                AgentRole.REVIEWER,
            )

        elif task_type == "model_training":

            agents = (
                AgentRole.ARCHITECT,
                AgentRole.ML_SCIENTIST,
                AgentRole.ENGINEER,
                AgentRole.REVIEWER,
            )

        elif task_type == "review":

            agents = (AgentRole.REVIEWER,)

        elif task_type == "research":

            agents = (AgentRole.RESEARCHER,)

        elif task_type in ("full_lifecycle", "all_agents", "enterprise_suite"):
            agents = (
                AgentRole.PROJECT_INTELLIGENCE,
                AgentRole.RESEARCHER,
                AgentRole.RND,
                AgentRole.ARCHITECT,
                AgentRole.ML_SCIENTIST,
                AgentRole.ENGINEER,
                AgentRole.QA,
                AgentRole.REVIEWER,
                AgentRole.RUNTIME_OBSERVER,
            )
        else:

            agents = (AgentRole.ARCHITECT,)

        return ExecutionPlan(
            task=request.task,
            agents=agents,
            metadata={
                "task_type": task_type,
                "project_id": (str(request.project_id) if request.project_id else None),
            },
        )

    def create_plan(self, task: Any, **kwargs: Any) -> ExecutionPlan:
        from uuid import uuid4
        from agentplatform.domain.planning import PlanningRequest
        request = PlanningRequest(
            project_id=getattr(task, "project_id", None) or uuid4(),
            task=task,
        )
        return self.plan(request)
