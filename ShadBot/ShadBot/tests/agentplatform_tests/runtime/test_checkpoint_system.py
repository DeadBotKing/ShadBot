"""
ShadBot Agent Platform

Unit tests for 7.5 Checkpoint System.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.runtime.checkpoint_system import (
    CheckpointCreator,
    CheckpointRestoreManager,
    CheckpointStorage,
    CheckpointSystemServiceLayer,
    CheckpointValidator,
    CheckpointVersioning,
)


def test_checkpoint_creator_creates_entity() -> None:
    pid = uuid4()
    cp = CheckpointCreator().create(pid, uuid4(), 1, 1, {"k": "v"})
    assert cp.step_number == 1
    assert cp.snapshot_data == {"k": "v"}


def test_checkpoint_storage_saves_and_latest() -> None:
    store = CheckpointStorage()
    pid = uuid4()
    cp1 = CheckpointCreator().create(pid, uuid4(), 1, 1, {"k": 1})
    cp2 = CheckpointCreator().create(pid, uuid4(), 2, 2, {"k": 2})
    store.save_checkpoint(cp1)
    store.save_checkpoint(cp2)
    assert store.load_latest(pid) == cp2


def test_checkpoint_versioning_increments() -> None:
    ver = CheckpointVersioning()
    assert ver.next_version(()) == 1
    cp = CheckpointCreator().create(uuid4(), uuid4(), 1, 3, {"k": 1})
    assert ver.next_version((cp,)) == 4


def test_checkpoint_system_service_layer_creates_and_restores() -> None:
    service = CheckpointSystemServiceLayer()
    pid = uuid4()
    saved, v = service.create_and_save(pid, uuid4(), 5, {"phase": "arch"})
    assert v == 1
    restored = service.restore_latest(pid)
    assert restored is not None
    assert restored.restored is True
    assert restored.data["phase"] == "arch"
