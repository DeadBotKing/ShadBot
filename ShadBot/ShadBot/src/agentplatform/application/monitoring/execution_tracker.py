"""
ShadBot Agent Platform

Execution tracker.
"""

from __future__ import annotations

from datetime import datetime, timezone

from agentplatform.domain.execution import (
    AgentExecution,
    ExecutionStatus,
    ExecutionStep,
)


class ExecutionTracker:
    """
    Tracks live agent execution state.
    """

    def create(
        self,
        task_name: str,
    ) -> AgentExecution:
        """
        Create new execution.
        """

        return AgentExecution(
            task_name=task_name,
        )

    def start_step(
        self,
        execution: AgentExecution,
        agent_name: str,
        action: str,
        step_number: int,
        total_steps: int,
    ) -> ExecutionStep:
        """
        Register running agent step.
        """

        step = ExecutionStep(
            step_number=step_number,
            total_steps=total_steps,
            agent_name=agent_name,
            action=action,
            status=ExecutionStatus.RUNNING,
            started_at=datetime.now(timezone.utc),
        )

        execution.add_step(
            step,
        )

        execution.status = ExecutionStatus.RUNNING

        return step

    def complete_step(
        self,
        step: ExecutionStep,
    ) -> None:
        """
        Complete step.
        """

        step.status = ExecutionStatus.COMPLETED

        step.completed_at = datetime.now(timezone.utc)

    def fail_step(
        self,
        step: ExecutionStep,
    ) -> None:
        """
        Fail step.
        """

        step.status = ExecutionStatus.FAILED

        step.completed_at = datetime.now(timezone.utc)
