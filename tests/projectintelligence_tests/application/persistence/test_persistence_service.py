"""
ShadBot Project Intelligence

Persistence Service Test
"""

from __future__ import annotations

from unittest.mock import Mock

from projectintelligence.application.persistence.services.persistence_service import (
    PersistenceService,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)


def test_persistence_service_delegates_storage_operations() -> None:

    snapshot_storage = Mock()
    context_storage = Mock()
    knowledge_storage = Mock()
    state_storage = Mock()
    resume_storage = Mock()
    history_storage = Mock()

    service = PersistenceService(
        snapshot_storage=snapshot_storage,
        context_storage=context_storage,
        knowledge_storage=knowledge_storage,
        state_storage=state_storage,
        resume_storage=resume_storage,
        history_storage=history_storage,
    )

    snapshot = Mock()
    context = Mock()
    knowledge = Mock()
    state = Mock()
    resume = Mock()
    history = SnapshotHistory()

    service.save_snapshot(
        snapshot,
    )

    service.save_context(
        context,
    )

    service.save_knowledge(
        knowledge,
    )

    service.save_state(
        state,
    )

    service.save_resume(
        resume,
    )

    service.save_history(
        history,
    )

    snapshot_storage.save.assert_called_once_with(
        snapshot,
    )

    context_storage.save.assert_called_once_with(
        context,
    )

    knowledge_storage.save.assert_called_once_with(
        knowledge,
    )

    state_storage.save.assert_called_once_with(
        state,
    )

    resume_storage.save.assert_called_once_with(
        resume,
    )

    history_storage.save.assert_called_once_with(
        history,
    )

def test_persistence_service_save_all_returns_batch_result() -> None:

    snapshot_storage = Mock()
    context_storage = Mock()
    knowledge_storage = Mock()
    state_storage = Mock()
    resume_storage = Mock()
    history_storage = Mock()

    service = PersistenceService(
        snapshot_storage=snapshot_storage,
        context_storage=context_storage,
        knowledge_storage=knowledge_storage,
        state_storage=state_storage,
        resume_storage=resume_storage,
        history_storage=history_storage,
    )

    snapshot_storage.save.return_value = Mock(success=True)
    context_storage.save.return_value = Mock(success=True)
    knowledge_storage.save.return_value = Mock(success=True)
    state_storage.save.return_value = Mock(success=True)
    resume_storage.save.return_value = Mock(success=True)
    history_storage.save.return_value = Mock(success=True)

    result = service.save_all(
        snapshot=Mock(),
        knowledge=Mock(),
        history=Mock(),
        state=Mock(),
        context=Mock(),
        resume=Mock(),
    )

    assert result.success is True

    assert len(
        result.results,
    ) == 6