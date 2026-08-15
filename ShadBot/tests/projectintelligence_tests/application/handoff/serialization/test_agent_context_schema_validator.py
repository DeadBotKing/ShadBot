"""
ShadBot Project Intelligence

Agent Context Schema Validator Tests
"""

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from projectintelligence.application.handoff.serialization.agent_context_schema_validator import (
    AgentContextSchemaValidator,
)
from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


def test_agent_context_schema_validator_accepts_valid_package():

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
        dependencies={
            "django": "6.0",
        },
        architecture_description="Clean Architecture",
        conventions=("CamelCase",),
        constraints=("Open source only",),
        recommendations=("Improve coverage",),
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

    validator = AgentContextSchemaValidator(
        schema_path=schema_path,
    )

    validator.validate_package(
        package,
    )
