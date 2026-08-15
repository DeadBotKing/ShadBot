"""
ShadBot Project Intelligence

Persistence Service Agent Context Tests
"""

from unittest.mock import Mock
from uuid import uuid4

from projectintelligence.application.persistence.services.persistence_service import (
    PersistenceService,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


def test_persistence_service_delegates_agent_context_storage():

    agent_context_storage = Mock()

    evolution_storage = Mock()

    service = PersistenceService(
        snapshot_storage=Mock(),
        context_storage=Mock(),
        knowledge_storage=Mock(),
        state_storage=Mock(),
        resume_storage=Mock(),
        history_storage=Mock(),
        agent_context_storage=agent_context_storage,
        evolution_storage=evolution_storage,
    )

    agent_context = AgentContextPackage(
        project_id=uuid4(),
        metadata=Mock(),
        summary="Agent context",
    )

    service.save_agent_context(
        agent_context,
    )

    agent_context_storage.save.assert_called_once_with(
        agent_context,
    )
