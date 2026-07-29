"""
ShadBot Project Intelligence

In Memory Agent Context Repository Tests
"""

from datetime import datetime, timezone
from uuid import uuid4

from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)
from projectintelligence.infrastructure.persistence.agent_context.in_memory_agent_context_repository import (
    InMemoryAgentContextRepository,
)
from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)


def test_in_memory_agent_context_repository_stores_context():
    repository = InMemoryAgentContextRepository()

    project_id = uuid4()

    package = AgentContextPackage(
        project_id=project_id,
        metadata=AgentContextMetadata(
            context_id=uuid4(),
            created_at=datetime.now(timezone.utc),
            version="1.0",
        ),
        summary="Test agent context",
    )

    repository.save(
        package,
    )

    result = repository.get_latest(
        project_id,
    )

    assert result == package


def test_in_memory_agent_context_repository_get_latest_returns_latest():
    repository = InMemoryAgentContextRepository()

    project_id = uuid4()

    first = AgentContextPackage(
        project_id=project_id,
        metadata=AgentContextMetadata(
            context_id=uuid4(),
            created_at=datetime.now(timezone.utc),
            version="1.0",
        ),
        summary="First context",
    )

    second = AgentContextPackage(
        project_id=project_id,
        metadata=AgentContextMetadata(
            context_id=uuid4(),
            created_at=datetime.now(timezone.utc),
            version="1.0",
        ),
        summary="Second context",
    )

    repository.save(first)
    repository.save(second)

    result = repository.get_latest(
        project_id,
    )

    assert result == second