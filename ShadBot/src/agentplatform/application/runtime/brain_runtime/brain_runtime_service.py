"""
ShadBot Agent Platform

Unified service for 7.2 Brain Runtime.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4
from .brain_runtime_instance import BrainRuntimeInstance, BrainRuntimeState
from .context_runtime import BrainContextRuntime, BrainContextSnapshot
from .reasoning_runtime import ReasoningRuntimeManager, ReasoningRuntimePackage
from .state_sync import BrainStateSynchronizer


class BrainRuntimeServiceLayer:
    """
    Orchestrates brain runtime instance lifecycle, reasoning preparation, and context snapshotting.
    """

    def __init__(
        self,
        reasoning_mgr: ReasoningRuntimeManager | None = None,
        context_rt: BrainContextRuntime | None = None,
        sync: BrainStateSynchronizer | None = None,
    ) -> None:
        self._reasoning_mgr = reasoning_mgr or ReasoningRuntimeManager()
        self._context_rt = context_rt or BrainContextRuntime()
        self._sync = sync or BrainStateSynchronizer()

    def start_brain(self, project_id: UUID, role_name: str, context_data: dict[str, Any]) -> tuple[BrainRuntimeInstance, ReasoningRuntimePackage, BrainContextSnapshot]:
        rid = uuid4()
        state = BrainRuntimeState(rid, "REASONING", "")
        inst = BrainRuntimeInstance(rid, state)
        active_inst = self._sync.synchronize(inst, "REASONING")
        reas_pkg = self._reasoning_mgr.prepare_reasoning(role_name, context_data)
        snap = self._context_rt.create_snapshot(project_id, context_data)
        return active_inst, reas_pkg, snap
