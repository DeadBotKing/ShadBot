"""
ShadBot Project Intelligence

Agent Context Package Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)
from projectintelligence.domain.handoff.evolution_summary import (
    EvolutionSummary,
)


@dataclass(frozen=True, slots=True)
class AgentContextPackage:
    """
    Stable knowledge package exposed to Agent Platform.

    This model is the boundary between:
    Project Intelligence Engine
    and
    Autonomous Coding Agents.

    Agents consume this package only and must not depend
    on internal Project Intelligence implementation details.
    """

    project_id: UUID

    metadata: AgentContextMetadata

    summary: str

    technologies: tuple[str, ...] = field(
        default_factory=tuple,
    )

    frameworks: tuple[str, ...] = field(
        default_factory=tuple,
    )

    languages: tuple[str, ...] = field(
        default_factory=tuple,
    )

    dependencies: dict[str, str] = field(
        default_factory=dict,
    )

    architecture_description: str | None = None

    conventions: tuple[str, ...] = field(
        default_factory=tuple,
    )

    constraints: tuple[str, ...] = field(
        default_factory=tuple,
    )

    recommendations: tuple[str, ...] = field(
        default_factory=tuple,
    )

    current_state: str | None = None

    evolution: EvolutionSummary | None = None
