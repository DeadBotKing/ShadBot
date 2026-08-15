"""
ShadBot Agent Platform

Unified service for 7.6 Resume System.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID
from agentplatform.application.runtime.checkpoint_system import CheckpointSystemServiceLayer
from .context_loader import ResumeContextLoader
from .continuation_manager import ContinuedExecutionPackage, ExecutionContinuationManager
from .recovery_engine import ExecutionRecoveryEngine, ExecutionRecoveryState
from .resume_request import ResumeRequest
from .resume_validation import ResumeValidationResult, ResumeValidator
from .state_restoration import StateRestoration


class ResumeSystemServiceLayer:
    """
    Orchestrates resume request processing, context loading, recovery, state restoration, validation, and continuation.
    """

    def __init__(
        self,
        checkpoint_service: CheckpointSystemServiceLayer | None = None,
        loader: ResumeContextLoader | None = None,
        engine: ExecutionRecoveryEngine | None = None,
        restoration: StateRestoration | None = None,
        validator: ResumeValidator | None = None,
        continuation_mgr: ExecutionContinuationManager | None = None,
    ) -> None:
        self._cp_service = checkpoint_service or CheckpointSystemServiceLayer()
        self._loader = loader or ResumeContextLoader()
        self._engine = engine or ExecutionRecoveryEngine()
        self._restoration = restoration or StateRestoration()
        self._validator = validator or ResumeValidator()
        self._continuation_mgr = continuation_mgr or ExecutionContinuationManager()

    def resume(self, request: ResumeRequest) -> ContinuedExecutionPackage | None:
        restored_pkg = self._cp_service.restore_latest(request.project_id)
        if restored_pkg is None:
            return None
        cp = restored_pkg.checkpoint
        ctx = self._loader.load_context(cp)
        rec = self._engine.recover_execution(cp, ctx)
        self._restoration.restore_state(cp.project_id, cp.session_id)
        val = self._validator.validate(rec)
        if not val.valid_resume:
            raise RuntimeError(val.notes)
        return self._continuation_mgr.continue_execution(rec)
