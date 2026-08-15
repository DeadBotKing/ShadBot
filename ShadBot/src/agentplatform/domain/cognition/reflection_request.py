"""
ShadBot Agent Platform

Reflection request contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from agentplatform.domain.results import AgentResult

from .reflection_type import ReflectionType


@dataclass(frozen=True, slots=True)
class ReflectionRequest:
    """
    Input contract for reflection execution.
    """

    results: tuple[AgentResult, ...]

    reflection_type: ReflectionType = ReflectionType.EXECUTION

    project_id: UUID | None = None

    metadata: dict[str, object] = field(
        default_factory=dict,
    )
