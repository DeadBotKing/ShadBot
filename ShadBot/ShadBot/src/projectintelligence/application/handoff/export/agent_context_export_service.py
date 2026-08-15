"""
ShadBot Project Intelligence

Agent Context Export Service
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.handoff.serialization.agent_context_schema_validator import (
    AgentContextSchemaValidator,
)
from projectintelligence.application.handoff.serialization.agent_context_serializer import (
    AgentContextSerializer,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


@dataclass(slots=True)
class AgentContextExportService:
    """
    Produces validated Agent Context payloads for external consumers.
    """

    serializer: AgentContextSerializer

    validator: AgentContextSchemaValidator

    def export(
        self,
        package: AgentContextPackage,
    ) -> dict[str, object]:
        """
        Export a validated Agent Context payload.
        """

        self.validator.validate_package(
            package,
        )

        return self.serializer.serialize(
            package,
        )

    @classmethod
    def create(
        cls,
        schema_path: Path,
    ) -> "AgentContextExportService":
        """
        Create a fully configured export service.
        """

        serializer = AgentContextSerializer()

        validator = AgentContextSchemaValidator(
            schema_path=schema_path,
        )

        return cls(
            serializer=serializer,
            validator=validator,
        )
