"""
ShadBot Agent Platform

Capability Execution Result Handler
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID

from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)


@dataclass(frozen=True, slots=True)
class CapabilityExecutionResult:
    """
    Standard execution result produced by capability engine.
    """

    execution_id: UUID

    agent_role: AgentRole

    capability: AgentCapability

    success: bool

    output: object | None = None

    error: str | None = None

    metadata: dict[str, object] | None = None

    executed_at: datetime = datetime.now(
        timezone.utc,
    )


class ExecutionResultHandler:
    """
    Handles capability execution results.
    """

    def handle_success(
        self,
        *,
        execution_id: UUID,
        agent_role: AgentRole,
        capability: AgentCapability,
        output: object,
        metadata: dict[str, object] | None = None,
    ) -> CapabilityExecutionResult:
        """
        Create successful execution result.
        """

        return CapabilityExecutionResult(
            execution_id=execution_id,
            agent_role=agent_role,
            capability=capability,
            success=True,
            output=output,
            metadata=metadata or {},
        )

    def handle_failure(
        self,
        *,
        execution_id: UUID,
        agent_role: AgentRole,
        capability: AgentCapability,
        error: Exception | str,
        metadata: dict[str, object] | None = None,
    ) -> CapabilityExecutionResult:
        """
        Create failed execution result.
        """

        return CapabilityExecutionResult(
            execution_id=execution_id,
            agent_role=agent_role,
            capability=capability,
            success=False,
            error=str(error),
            metadata=metadata or {},
        )

    def normalize(
        self,
        *,
        execution_id: UUID,
        agent_role: AgentRole,
        capability: AgentCapability,
        result: object,
    ) -> CapabilityExecutionResult:
        """
        Normalize unknown execution outputs.
        """

        if isinstance(
            result,
            CapabilityExecutionResult,
        ):
            return result

        return CapabilityExecutionResult(
            execution_id=execution_id,
            agent_role=agent_role,
            capability=capability,
            success=True,
            output=result,
        )
