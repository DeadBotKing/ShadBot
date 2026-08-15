"""
ShadBot Agent Platform

Unit tests for 7.1 Agent Runtime.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.runtime.agent_runtime import (
    AgentLifecycleManager,
    AgentProcessController,
    AgentRuntimeMonitor,
    AgentRuntimeServiceLayer,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.infrastructure.agents import ArchitectAgent


def test_lifecycle_manager_creates_and_starts() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    mgr = AgentLifecycleManager()
    inst = mgr.create_instance(arch)
    assert inst.state.status == "CREATED"
    started = mgr.start_instance(inst)
    assert started.state.status == "RUNNING"


def test_process_controller_executes_safely() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    inst = AgentLifecycleManager().start_instance(AgentLifecycleManager().create_instance(arch))
    ctx = AgentExecutionContext(uuid4(), uuid4(), "test")
    res = AgentProcessController().execute_instance(inst, ctx)
    assert res.success is True


def test_runtime_monitor_inspects_health() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    inst = AgentLifecycleManager().start_instance(AgentLifecycleManager().create_instance(arch))
    health = AgentRuntimeMonitor().inspect(inst)
    assert health.is_active is True


def test_agent_runtime_service_layer_runs_agent() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    ctx = AgentExecutionContext(uuid4(), uuid4(), "test")
    res, health = AgentRuntimeServiceLayer().run_agent(arch, ctx)
    assert res.success is True
    assert health.status == "COMPLETED"
