"""
ShadBot Agent Platform

Agent execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


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

    intelligence_context: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    execution_id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
