"""
ShadBot Agent Platform

Execution reporter.
"""

from __future__ import annotations

from agentplatform.domain.execution import (
    AgentExecution,
)


class ExecutionReporter:
    """
    Prints execution progress.
    """

    def report(
        self,
        execution: AgentExecution,
    ) -> None:
        """
        Print execution state.
        """

        total = len(
            execution.steps,
        )

        print(
            "",
        )

        print(
            f"Execution: {execution.execution_id}",
        )

        print(
            f"Task: {execution.task_name}",
        )

        print(
            f"Status: {execution.status.value}",
        )

        print(
            "",
        )

        for step in execution.steps:
            print(
                (
                    f"[{step.step_number}/{step.total_steps}] "
                    f"{step.agent_name.upper()} "
                    f"- {step.status.value}"
                ),
            )

        print(
            f"Completed steps: {total}",
        )

        print(
            "",
        )
