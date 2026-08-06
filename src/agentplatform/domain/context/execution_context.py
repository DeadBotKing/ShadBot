"""
ShadBot Agent Platform

Agent execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from agentplatform.domain.workspace import (
    Project,
    Workspace,
)


@dataclass(frozen=True, slots=True)
class AgentExecutionContext:
    """
    Runtime context provided to an agent.

    This object connects:
    - Agent
    - Task
    - Project Intelligence output
    - Runtime metadata
    """

    project_id: UUID

    task_id: UUID

    instructions: str

    workspace: Workspace | None = None

    target_project: Project | None = None

    task_title: str = ""

    task_description: str = ""

    task_type: str = ""

    intelligence_context: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    memory_context: dict[str, Any] = field(
        default_factory=dict,
    )

    execution_id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def with_memory_context(
        self,
        memory_context: dict[str, object],
    ) -> "AgentExecutionContext":
        """
        Create context copy with memory.
        """

        return AgentExecutionContext(
            project_id=self.project_id,
            task_id=self.task_id,
            instructions=self.instructions,
            workspace=self.workspace,
            target_project=self.target_project,
            task_title=self.task_title,
            task_description=self.task_description,
            task_type=self.task_type,
            intelligence_context=self.intelligence_context,
            metadata=self.metadata,
            memory_context=memory_context,
            execution_id=self.execution_id,
            created_at=self.created_at,
        )
