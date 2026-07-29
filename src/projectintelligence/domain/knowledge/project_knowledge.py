"""
ShadBot Project Intelligence

Project Knowledge Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from projectintelligence.domain.knowledge.knowledge_finding import (
    KnowledgeFinding,
)


@dataclass(slots=True)
class ProjectKnowledge:
    """
    Enterprise knowledge model generated from project analysis.
    """

    project_id: UUID

    knowledge_id: UUID = field(default_factory=uuid4)

    version: str = "1.0"

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    technologies: list[str] = field(default_factory=list)

    frameworks: list[str] = field(default_factory=list)

    languages: list[str] = field(default_factory=list)

    dependency_map: dict[str, str] = field(default_factory=dict)

    architecture_description: str | None = None

    architecture_patterns: list[str] = field(default_factory=list)

    project_conventions: list[str] = field(default_factory=list)

    coding_rules: list[str] = field(default_factory=list)

    known_constraints: list[str] = field(default_factory=list)

    historical_changes: list[str] = field(default_factory=list)

    intelligence_notes: list[str] = field(default_factory=list)

    findings: list[KnowledgeFinding] = field(default_factory=list)
