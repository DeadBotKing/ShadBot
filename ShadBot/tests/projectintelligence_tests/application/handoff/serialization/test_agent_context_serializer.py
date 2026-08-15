"""
ShadBot Project Intelligence

Agent Context Serializer Tests
"""

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from projectintelligence.application.handoff.serialization.agent_context_serializer import (
    AgentContextSerializer,
)
from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


def test_agent_context_serializer_serializes_package():

    package = AgentContextPackage(
        project_id=uuid4(),
        metadata=AgentContextMetadata(
            context_id=uuid4(),
            version="1.0",
            contract_version="1.0",
            created_at=datetime.now(timezone.utc),
        ),
        summary="Test project",
        technologies=("Python",),
        frameworks=("Django",),
        languages=("Python",),
        dependencies={
            "django": "6.0",
        },
        architecture_description="Clean Architecture",
        conventions=("CamelCase",),
        constraints=("No paid APIs",),
        recommendations=("Add tests",),
        current_state="Phase 1",
    )

    serializer = AgentContextSerializer()

    result: dict[str, Any] = serializer.serialize(
        package,
    )

    assert result["project_id"]
    assert result["summary"] == "Test project"
    assert result["technologies"] == ["Python"]
    assert result["frameworks"] == ["Django"]
    assert result["dependencies"]["django"] == "6.0"

    assert result["metadata"]["contract_version"] == "1.0"
    assert result["metadata"]["context_id"]
    assert result["metadata"]["created_at"]
