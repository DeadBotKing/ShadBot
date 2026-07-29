"""
ShadBot Project Intelligence

Agent Context Export Service Tests
"""

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from projectintelligence.application.handoff.export.agent_context_export_service import (
    AgentContextExportService,
)
from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


def test_export_service_exports_valid_payload():

    package = AgentContextPackage(
        project_id=uuid4(),
        metadata=AgentContextMetadata(
            context_id=uuid4(),
            version="1.0",
            contract_version="1.0",
            created_at=datetime.now(timezone.utc),
        ),
        summary="Project analysis completed.",
        technologies=("Python",),
        frameworks=("Django",),
        languages=("Python",),
        dependencies={"django": "6.0"},
        architecture_description="Clean Architecture",
        conventions=("CamelCase",),
        constraints=("Open source only",),
        recommendations=("Increase test coverage",),
        current_state="Development",
    )

    schema_path = (
        Path(__file__).parents[5]
        / "src"
        / "projectintelligence"
        / "application"
        / "handoff"
        / "schemas"
        / "agent_context_schema.json"
    )

    service = AgentContextExportService.create(
        schema_path=schema_path,
    )

    payload = service.export(
        package,
    )

    assert payload["summary"] == "Project analysis completed."
    assert payload["metadata"]["contract_version"] == "1.0"
    assert payload["frameworks"] == ["Django"]
