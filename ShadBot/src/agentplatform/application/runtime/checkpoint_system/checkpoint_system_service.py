"""
ShadBot Agent Platform

Unified service for 7.5 Checkpoint System.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID
from .checkpoint_creator import CheckpointCreator
from .checkpoint_entity import CheckpointEntity
from .checkpoint_restore import CheckpointRestoreManager, RestoredCheckpointPackage
from .checkpoint_storage import CheckpointStorage
from .checkpoint_validation import CheckpointValidationResult, CheckpointValidator
from .checkpoint_versioning import CheckpointVersioning


class CheckpointSystemServiceLayer:
    """
    Orchestrates checkpoint creation, storage, versioning, validation, and restore.
    """

    def __init__(
        self,
        creator: CheckpointCreator | None = None,
        storage: CheckpointStorage | None = None,
        versioning: CheckpointVersioning | None = None,
        validator: CheckpointValidator | None = None,
        restore_mgr: CheckpointRestoreManager | None = None,
    ) -> None:
        self._creator = creator or CheckpointCreator()
        self._storage = storage or CheckpointStorage()
        self._versioning = versioning or CheckpointVersioning()
        self._validator = validator or CheckpointValidator()
        self._restore_mgr = restore_mgr or CheckpointRestoreManager(self._validator)

    def create_and_save(self, project_id: UUID, session_id: UUID, step_number: int, data: dict[str, Any]) -> tuple[CheckpointEntity, int]:
        existing = self._storage._checkpoints.get(project_id, [])
        v = self._versioning.next_version(existing)
        cp = self._creator.create(project_id, session_id, step_number, v, data)
        saved = self._storage.save_checkpoint(cp)
        return saved, v

    def restore_latest(self, project_id: UUID) -> RestoredCheckpointPackage | None:
        latest = self._storage.load_latest(project_id)
        if latest is None:
            return None
        return self._restore_mgr.restore(latest)
