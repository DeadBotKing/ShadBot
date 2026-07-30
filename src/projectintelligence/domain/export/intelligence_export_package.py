"""
ShadBot Project Intelligence

Intelligence Export Package Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.resume.project_state import (
    ProjectState,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(frozen=True, slots=True)
class IntelligenceExportPackage:
    """
    Complete export contract of Project Intelligence output.

    This object represents the final intelligence artifact
    consumed by external systems such as Agent Platform.
    """

    export_id: UUID

    project_id: UUID

    generated_at: datetime

    snapshot: ProjectSnapshot

    knowledge: ProjectKnowledge

    context: ProjectContext

    history: SnapshotHistory

    state: ProjectState
