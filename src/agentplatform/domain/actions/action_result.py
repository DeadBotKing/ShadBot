"""
ShadBot Agent Platform

Action Result Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from agentplatform.domain.actions.action import (
    ActionStatus,
)


@dataclass(frozen=True, slots=True)
class ActionResult:
    """
    Represents the result of an executed agent action.
    """

    action_id: UUID

    status: ActionStatus

    success: bool

    result: object | None = None

    error: str | None = None

    result_id: UUID = field(
        default_factory=uuid4,
    )

    execution_time_ms: int = 0

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    completed_at: datetime | None = None

    @classmethod
    def completed(
        cls,
        action_id: UUID,
        result: object,
        execution_time_ms: int = 0,
    ) -> "ActionResult":
        """
        Create successful action result.
        """

        now = datetime.now(
            timezone.utc,
        )

        return cls(
            action_id=action_id,
            status=ActionStatus.COMPLETED,
            success=True,
            result=result,
            error=None,
            execution_time_ms=execution_time_ms,
            completed_at=now,
        )

    @classmethod
    def failed(
        cls,
        action_id: UUID,
        error: str,
        execution_time_ms: int = 0,
    ) -> "ActionResult":
        """
        Create failed action result.
        """

        now = datetime.now(
            timezone.utc,
        )

        return cls(
            action_id=action_id,
            status=ActionStatus.FAILED,
            success=False,
            result=None,
            error=error,
            execution_time_ms=execution_time_ms,
            completed_at=now,
        )

    def is_successful(
        self,
    ) -> bool:
        """
        Check execution success.
        """

        return self.success and self.error is None
