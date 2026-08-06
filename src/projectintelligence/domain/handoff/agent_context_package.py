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

    dependencies: dict[str, str] = field(
        default_factory=dict,
    )

    risks: tuple[str, ...] = ()

    recommendations: tuple[str, ...] = ()

    extra: dict[str, Any] = field(
        default_factory=dict,
    )

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
