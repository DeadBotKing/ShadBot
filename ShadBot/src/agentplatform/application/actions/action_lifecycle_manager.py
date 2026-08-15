"""
ShadBot Agent Platform

Action Lifecycle Manager
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from agentplatform.domain.actions import (
    Action,
    ActionResult,
    ActionStatus,
)


@dataclass(slots=True)
class ActionLifecycleManager:
    """
    Manages lifecycle state transitions
    of agent actions.
    """

    def start(
        self,
        action: Action,
    ) -> Action:
        """
        Mark action as started.
        """

        return action.transition_to(
            ActionStatus.RUNNING,
            started_at=datetime.now(
                timezone.utc,
            ),
        )

    def complete(
        self,
        action: Action,
        result: object,
    ) -> ActionResult:
        """
        Complete action successfully.
        """

        completed_at = datetime.now(
            timezone.utc,
        )

        return ActionResult.completed(
            action_id=action.action_id,
            result=result,
        )

    def fail(
        self,
        action: Action,
        error: str,
    ) -> ActionResult:
        """
        Complete action with failure.
        """

        return ActionResult.failed(
            action_id=action.action_id,
            error=error,
        )

    def validate_transition(
        self,
        current_status: ActionStatus,
        target_status: ActionStatus,
    ) -> bool:
        """
        Validate allowed lifecycle transitions.
        """

        allowed = {
            ActionStatus.CREATED: {
                ActionStatus.RUNNING,
                ActionStatus.CANCELLED,
            },
            ActionStatus.RUNNING: {
                ActionStatus.COMPLETED,
                ActionStatus.FAILED,
                ActionStatus.CANCELLED,
            },
            ActionStatus.COMPLETED: set(),
            ActionStatus.FAILED: set(),
            ActionStatus.CANCELLED: set(),
        }

        return target_status in allowed.get(
            current_status,
            set(),
        )
