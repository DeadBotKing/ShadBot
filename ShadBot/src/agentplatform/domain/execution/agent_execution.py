"""
ShadBot Agent Platform

Agent execution model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from agentplatform.domain.execution.execution_status import (
    ExecutionStatus,
)
from agentplatform.domain.execution.execution_step import (
    ExecutionStep,
)


@dataclass(slots=True)
class AgentExecution:
    """
    Tracks one complete agent pipeline execution.
    """

    task_name: str

    execution_id: UUID = field(
        default_factory=uuid4,
    )

    status: ExecutionStatus = ExecutionStatus.CREATED

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    steps: list[ExecutionStep] = field(
        default_factory=list,
    )

    def add_step(
        self,
        step: ExecutionStep,
    ) -> None:
        """
        Add execution step.
        """

        step.execution_id = self.execution_id

        self.steps.append(
            step,
        )

    def complete(
        self,
    ) -> None:
        """
        Mark execution completed.
        """

        self.status = ExecutionStatus.COMPLETED

    def fail(
        self,
    ) -> None:
        """
        Mark execution failed.
        """

        self.status = ExecutionStatus.FAILED
