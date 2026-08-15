"""
ShadBot Agent Platform

Execution step model.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from agentplatform.domain.execution.execution_status import (
    ExecutionStatus,
)


@dataclass(slots=True)
class ExecutionStep:
    """
    Represents one agent execution step.
    """

    step_number: int

    total_steps: int

    agent_name: str

    action: str

    status: ExecutionStatus

    started_at: datetime | None = None

    completed_at: datetime | None = None

    execution_id: UUID | None = None
