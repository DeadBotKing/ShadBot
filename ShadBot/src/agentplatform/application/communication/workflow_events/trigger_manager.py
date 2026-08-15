"""
ShadBot Agent Platform

Workflow Trigger Manager component for 8.3 Workflow Events.
"""

from __future__ import annotations

from typing import Callable
from uuid import UUID
from .workflow_event import WorkflowEvent


class WorkflowTriggerManager:
    """
    Detects workflow state triggers and initiates reactions.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[[WorkflowEvent], None]]] = {}

    def register_trigger(self, state: str, handler: Callable[[WorkflowEvent], None]) -> None:
        if state not in self._handlers:
            self._handlers[state] = []
        self._handlers[state].append(handler)

    def trigger(self, event: WorkflowEvent) -> int:
        handlers = self._handlers.get(event.state, [])
        for handler in handlers:
            try:
                handler(event)
            except Exception:
                continue
        return len(handlers)
