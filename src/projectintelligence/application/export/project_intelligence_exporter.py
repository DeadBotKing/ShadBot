"""
ShadBot Project Intelligence

Project Intelligence Exporter
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from projectintelligence.application.export.agent_context_export_serializer import (
    AgentContextExportSerializer,
)
from projectintelligence.application.export.context_serializer import (
    ContextSerializer,
)
from projectintelligence.application.export.evolution_serializer import (
    EvolutionSerializer,
)
from projectintelligence.application.export.knowledge_serializer import (
    KnowledgeSerializer,
)
from projectintelligence.application.export.resume_serializer import (
    ResumeSerializer,
)
from projectintelligence.application.export.snapshot_serializer import (
    SnapshotSerializer,
)
from projectintelligence.application.export.state_serializer import (
    StateSerializer,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)


@dataclass(slots=True)
class ProjectIntelligenceExporter:
    """
    Exports complete Project Intelligence result.
    """

    snapshot_serializer: SnapshotSerializer
    knowledge_serializer: KnowledgeSerializer
    context_serializer: ContextSerializer
    state_serializer: StateSerializer
    resume_serializer: ResumeSerializer
    agent_context_serializer: AgentContextExportSerializer | None = None
    evolution_serializer: EvolutionSerializer | None = None

    def export(
        self,
        result: PipelineResult,
        output_path: Path,
    ) -> Path:
        """
        Export pipeline result into JSON artifact.
        """

        payload: dict[str, Any] = {
            "snapshot": self.snapshot_serializer.serialize(
                result.snapshot,
            ),
            "knowledge": self.knowledge_serializer.serialize(
                result.knowledge,
            ),
            "context": self.context_serializer.serialize(
                result.context,
            ),
            "state": self.state_serializer.serialize(
                result.state,
            ),
        }

        if result.resume is not None:
            payload["resume"] = self.resume_serializer.serialize(
                result.resume,
            )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if (
            result.agent_context is not None
            and self.agent_context_serializer is not None
        ):
            payload["agent_context"] = self.agent_context_serializer.serialize(
                result.agent_context,
            )

        if result.evolution is not None and self.evolution_serializer is not None:
            payload["evolution"] = self.evolution_serializer.serialize(
                result.evolution,
            )

        output_path.write_text(
            json.dumps(
                payload,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return output_path
