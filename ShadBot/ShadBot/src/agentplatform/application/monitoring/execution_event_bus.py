"""
ShadBot Agent Platform

Execution event bus.
"""

from __future__ import annotations

from collections.abc import Callable

from agentplatform.domain.execution import (
    ExecutionEvent,
)

ExecutionEventListener = Callable[
    [ExecutionEvent],
    None,
]


class ExecutionEventBus:
    """
    Publishes execution events to listeners.
    """

    def __init__(self) -> None:
        self._listeners: list[ExecutionEventListener] = []

    def subscribe(
        self,
        listener: ExecutionEventListener,
    ) -> None:
        """
        Register execution event listener.
        """

        self._listeners.append(
            listener,
        )

    def publish(
        self,
        event: ExecutionEvent,
    ) -> None:
        """
        Publish event to all listeners.
        """

        for listener in self._listeners:
            listener(event)
