"""
ShadBot Agent Platform

Action Dispatcher
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.capabilities import (
    CapabilityExecutor,
)
from agentplatform.domain.actions import (
    Action,
    ActionRequest,
    ActionResult,
)


@dataclass(slots=True)
class ActionDispatcher:
    """
    Dispatches agent action requests
    to capability execution engine.
    """

    executor: CapabilityExecutor

    def dispatch(
        self,
        request: ActionRequest,
    ) -> ActionResult:
        """
        Dispatch action request.
        """

        action = Action(
            agent_role=request.agent_role,
            capability=request.capability,
            input_payload=request.payload,
        )

        return self._execute(
            action,
        )

    def _execute(
        self,
        action: Action,
    ) -> ActionResult:
        """
        Execute action through capability executor.
        """

        try:
            result = self.executor.execute(
                action,
            )

            if isinstance(
                result,
                ActionResult,
            ):
                return result

            return ActionResult.completed(
                action_id=action.action_id,
                result=result,
            )

        except Exception as exc:
            return ActionResult.failed(
                action_id=action.action_id,
                error=str(exc),
            )
