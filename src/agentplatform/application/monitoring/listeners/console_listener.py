"""
ShadBot Agent Platform

Console execution listener.
"""

from __future__ import annotations

from agentplatform.domain.execution import (
    ExecutionEvent,
)


class ConsoleExecutionListener:
    """
    Prints execution events to console.
    """

    def __call__(
        self,
        event: ExecutionEvent,
    ) -> None:
        """
        Handle execution event.
        """

        print(
            "",
        )

        print(
            "==============================",
        )

        print(
            f"EVENT: {event.event_type}",
        )

        print(
            f"AGENT: {event.agent_name}",
        )

        print(
            f"MESSAGE: {event.message}",
        )

        if event.metadata:
            print(
                f"DATA: {event.metadata}",
            )

        print(
            "==============================",
        )

        print(
            "",
        )
