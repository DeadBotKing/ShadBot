"""
ShadBot Agent Platform

Brain execution context model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class BrainContext:
    """
    Unified cognitive context provided to Agent Brain.

    Contains:
    - Project Intelligence
    - Memory
    - Goals
    - Attention selected context
    - Planning
    - Decision
    - Reflection
    - Validation
    - Profile
    - Learning data
    """

    project_id: UUID

    project_intelligence: dict[str, Any] = field(
        default_factory=dict,
    )

    memory_context: dict[str, Any] = field(
        default_factory=dict,
    )

    goal_context: dict[str, Any] = field(
        default_factory=dict,
    )

    attention_context: dict[str, Any] = field(
        default_factory=dict,
    )

    planning_context: dict[str, Any] = field(
        default_factory=dict,
    )

    reasoning_context: dict[str, Any] = field(
        default_factory=dict,
    )

    decision_context: dict[str, Any] = field(
        default_factory=dict,
    )

    reflection_context: dict[str, Any] = field(
        default_factory=dict,
    )

    validation_context: dict[str, Any] = field(
        default_factory=dict,
    )

    profile_context: dict[str, Any] = field(
        default_factory=dict,
    )

    learning_context: dict[str, Any] = field(
        default_factory=dict,
    )

    context_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
