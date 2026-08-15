"""
ShadBot Agent Platform

Queued task.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.tasks import AgentTask


@dataclass(frozen=True, slots=True)
class QueuedTask:
    """
    Task waiting for execution.
    """

    priority: int

    task: AgentTask
