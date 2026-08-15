"""
ShadBot Agent Platform

Capability Execution Lifecycle Management
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)

from .execution_context_injector import (
    CapabilityExecutionContext,
)


class ExecutionLifecycleStatus(str, Enum):
    """
    Capability execution states.
    """

    CREATED = "created"

    CONTEXT_READY = "context_ready"

    RESOLVED = "resolved"

    EXECUTING = "executing"

    COMPLETED = "completed"

    FAILED = "failed"


@dataclass(slots=True)
class CapabilityExecutionLifecycle:
    """
    Tracks lifecycle of capability execution.
    """

    agent_role: AgentRole

    capability: AgentCapability

    project_id: UUID

    execution_id: UUID = uuid4()

    status: ExecutionLifecycleStatus = ExecutionLifecycleStatus.CREATED

    started_at: datetime = datetime.now(timezone.utc)

    completed_at: datetime | None = None

    error: str | None = None

    context: CapabilityExecutionContext | None = None

    def attach_context(
        self,
        context: CapabilityExecutionContext,
    ) -> None:
        """
        Attach execution context.
        """

        self.context = context

        self.status = ExecutionLifecycleStatus.CONTEXT_READY

    def mark_resolved(
        self,
    ) -> None:
        """
        Mark capability and tool resolved.
        """

        self.status = ExecutionLifecycleStatus.RESOLVED

    def start(
        self,
    ) -> None:
        """
        Start execution.
        """

        self.status = ExecutionLifecycleStatus.EXECUTING

    def complete(
        self,
    ) -> None:
        """
        Complete execution successfully.
        """

        self.status = ExecutionLifecycleStatus.COMPLETED

        self.completed_at = datetime.now(
            timezone.utc,
        )

    def fail(
        self,
        error: str,
    ) -> None:
        """
        Mark execution failure.
        """

        self.status = ExecutionLifecycleStatus.FAILED

        self.error = error

        self.completed_at = datetime.now(
            timezone.utc,
        )


class ExecutionLifecycleManager:
    """
    Creates and manages capability execution lifecycle.
    """

    def create(
        self,
        *,
        agent_role: AgentRole,
        capability: AgentCapability,
        project_id: UUID,
    ) -> CapabilityExecutionLifecycle:
        """
        Create new lifecycle instance.
        """

        return CapabilityExecutionLifecycle(
            agent_role=agent_role,
            capability=capability,
            project_id=project_id,
        )

    def prepare(
        self,
        lifecycle: CapabilityExecutionLifecycle,
        context: CapabilityExecutionContext,
    ) -> None:
        """
        Prepare execution context.
        """

        lifecycle.attach_context(
            context,
        )

    def begin(
        self,
        lifecycle: CapabilityExecutionLifecycle,
    ) -> None:
        """
        Start capability execution.
        """

        lifecycle.start()

    def finish(
        self,
        lifecycle: CapabilityExecutionLifecycle,
    ) -> None:
        """
        Mark execution successful.
        """

        lifecycle.complete()

    def fail(
        self,
        lifecycle: CapabilityExecutionLifecycle,
        error: Exception,
    ) -> None:
        """
        Handle execution failure.
        """

        lifecycle.fail(
            str(error),
        )
