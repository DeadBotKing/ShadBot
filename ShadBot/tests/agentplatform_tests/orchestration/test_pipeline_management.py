"""
ShadBot Agent Platform

Unit tests for 6.3 Pipeline Management.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.orchestration.pipeline_management import (
    PipelineBuilder,
    PipelineCompletionDetector,
    PipelineDependencyManager,
    PipelineManagementService,
    PipelineStateTracker,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.infrastructure.agents import ArchitectAgent, EngineerAgent


def test_pipeline_builder_creates_steps() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    pipe = PipelineBuilder().build_pipeline("MyTask", [arch])
    assert pipe.total_steps == 1
    assert pipe.steps[0].agent == arch


def test_state_tracker_records_progress() -> None:
    tracker = PipelineStateTracker()
    pid = uuid4()
    state = tracker.init_state(pid)
    assert state.status == "RUNNING"
    new_st = tracker.complete_step(pid, 1)
    assert 1 in new_st.completed_steps


def test_dependency_manager_checks_ready() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    pipe = PipelineBuilder().build_pipeline("Task", [arch])
    mgr = PipelineDependencyManager()
    assert mgr.is_step_ready(pipe.steps[0], ()) is True


def test_completion_detector_identifies_end() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    pipe = PipelineBuilder().build_pipeline("Task", [arch])
    tracker = PipelineStateTracker()
    st = tracker.init_state(pipe.pipeline_id)
    st_comp = tracker.complete_step(pipe.pipeline_id, 1)
    assert PipelineCompletionDetector().is_completed(pipe, st_comp) is True


def test_pipeline_management_service_orchestrates_flow() -> None:
    arch = ArchitectAgent(role=AgentRole.ARCHITECT)
    service = PipelineManagementService()
    pipe, state = service.create_pipeline("Task", [arch])
    new_st, done = service.advance_pipeline(pipe, 1)
    assert done is True
