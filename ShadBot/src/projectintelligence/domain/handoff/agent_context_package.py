"""
ShadBot Project Intelligence

Agent handoff package.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID

from .agent_context_metadata import (
    AgentContextMetadata,
)
from .project_architecture import (
    ProjectArchitecture,
)
from .project_state import (
    ProjectState,
)


@dataclass(frozen=True, slots=True)
class AgentContextPackage:
    """
    Complete project vision delivered to agents.
    """

    project_id: UUID
    metadata: AgentContextMetadata
    summary: str
    architecture: ProjectArchitecture
    state: ProjectState
    dependencies: dict[str, str]
    risks: tuple[str, ...]
    recommendations: tuple[str, ...]
    extra: dict[str, Any]

    def __init__(
        self,
        project_id: UUID,
        summary: str = "",
        metadata: AgentContextMetadata | None = None,
        architecture: ProjectArchitecture | None = None,
        state: ProjectState | None = None,
        dependencies: dict[str, str] | None = None,
        risks: tuple[str, ...] = (),
        recommendations: tuple[str, ...] = (),
        extra: dict[str, Any] | None = None,
        technologies: tuple[str, ...] = (),
        frameworks: tuple[str, ...] = (),
        languages: tuple[str, ...] = (),
        architecture_description: str = "",
        conventions: tuple[str, ...] = (),
        constraints: tuple[str, ...] = (),
        current_state: str | None = None,
        evolution: Any = None,
        **kwargs: Any,
    ) -> None:
        if metadata is None:
            metadata = AgentContextMetadata(project_id=project_id)
        if architecture is None:
            architecture = ProjectArchitecture(
                architecture_style=architecture_description,
                modules=(),
                frameworks=frameworks,
                languages=languages,
                conventions=conventions,
            )
        if state is None:
            state = ProjectState()
        if dependencies is None:
            dependencies = {}
        if extra is None:
            extra = {}
        extra.update({
            "technologies": technologies,
            "constraints": constraints,
            "evolution": evolution,
            "current_state": current_state,
        })
        object.__setattr__(self, "project_id", project_id)
        object.__setattr__(self, "metadata", metadata)
        object.__setattr__(self, "summary", summary)
        object.__setattr__(self, "architecture", architecture)
        object.__setattr__(self, "state", state)
        object.__setattr__(self, "dependencies", dependencies)
        object.__setattr__(self, "risks", risks)
        object.__setattr__(self, "recommendations", recommendations)
        object.__setattr__(self, "extra", extra)

    @property
    def technologies(self) -> tuple[str, ...]:
        return tuple(self.extra.get("technologies", ()))

    @property
    def frameworks(self) -> tuple[str, ...]:
        return self.architecture.frameworks

    @property
    def languages(self) -> tuple[str, ...]:
        return self.architecture.languages

    @property
    def architecture_description(self) -> str:
        return self.architecture.architecture_style

    @property
    def conventions(self) -> tuple[str, ...]:
        return self.architecture.conventions

    @property
    def constraints(self) -> tuple[str, ...]:
        return tuple(self.extra.get("constraints", ()))

    @property
    def current_state(self) -> str:
        if "current_state" in self.extra and self.extra["current_state"] is not None:
            return str(self.extra["current_state"])
        return str(getattr(self.state, "current_phase", getattr(self.state, "status", "active")))

    @property
    def evolution(self) -> Any:
        return self.extra.get("evolution")

    def to_dict(
        self,
    ) -> dict[str, object]:

        return {
            "project_id": str(
                self.project_id,
            ),
            "metadata": self.metadata.to_dict(),
            "summary": self.summary,
            "architecture": (self.architecture.to_dict()),
            "state": (self.state.to_dict()),
            "dependencies": self.dependencies,
            "risks": list(
                self.risks,
            ),
            "recommendations": list(
                self.recommendations,
            ),
            "extra": self.extra,
        }
