"""
Agent execution service.

Application service responsible for coordinating agent execution.
"""

from __future__ import annotations

from agentplatform.application.execution.agent_executor import (
    AgentExecutor,
)
from agentplatform.application.monitoring import (
    ExecutionEventBus,
    ExecutionTracker,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.contracts import (
    AgentContract,
)
from agentplatform.domain.execution import (
    AgentExecution,
    ExecutionEvent,
    ExecutionStep,
)
from agentplatform.domain.results import (
    AgentResult,
)


class AgentExecutionService:
    """
    Coordinates execution flow of agents.
    """

    def __init__(
        self,
        executor: AgentExecutor | None = None,
        tracker: ExecutionTracker | None = None,
        event_bus: ExecutionEventBus | None = None,
    ) -> None:
        self._executor = executor or AgentExecutor()

        self._tracker = tracker or ExecutionTracker()

        self._event_bus = event_bus or ExecutionEventBus()

    def execute(
        self,
        agent: AgentContract,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute an agent through executor.
        """

        execution = self._get_execution(
            context,
        )

        step = None

        if execution is not None:
            step = self._start_step(
                execution,
                agent,
                context,
            )

        try:
            result = self._executor.execute(
                agent,
                context,
            )

            if step is not None and execution is not None:
                self._tracker.complete_step(
                    step,
                )

                self._publish_event(
                    execution,
                    agent,
                    "AGENT_COMPLETED",
                    "Agent execution completed.",
                )

            return result

        except Exception as exc:
            if step is not None and execution is not None:
                self._tracker.fail_step(
                    step,
                )

                self._publish_event(
                    execution,
                    agent,
                    "AGENT_FAILED",
                    str(exc),
                )

            raise

    def _get_execution(
        self,
        context: AgentExecutionContext,
    ) -> AgentExecution | None:
        """
        Extract execution tracking object.
        """

        execution = context.metadata.get(
            "agent_execution",
        )

        if isinstance(
            execution,
            AgentExecution,
        ):
            return execution

        return None

    def _start_step(
        self,
        execution: AgentExecution,
        agent: AgentContract,
        context: AgentExecutionContext,
    ) -> ExecutionStep:
        """
        Start tracking agent step.
        """

        total_steps = len(
            context.metadata.get(
                "planned_agents",
                [],
            ),
        )

        step_number = len(execution.steps) + 1

        step = self._tracker.start_step(
            execution,
            agent.name,
            "execute",
            step_number,
            max(total_steps, 1),
        )

        self._publish_event(
            execution,
            agent,
            "AGENT_STARTED",
            "Agent execution started.",
        )

        return step

    def _publish_event(
        self,
        execution: AgentExecution,
        agent: AgentContract,
        event_type: str,
        message: str,
    ) -> None:
        """
        Publish execution lifecycle event.
        """

        self._event_bus.publish(
            ExecutionEvent(
                execution_id=execution.execution_id,
                event_type=event_type,
                agent_name=agent.name,
                message=message,
            ),
        )
