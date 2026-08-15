"""
ShadBot Agent Platform

ML Scientist agent and experiment-executor contract tests.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from agentplatform.application.tooling import ToolExecutor, ToolRegistry
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.tooling import ToolDefinition
from agentplatform.domain.tools import ToolContract, ToolType
from agentplatform.domain.workspace import Project
from agentplatform.infrastructure.agents.ml_scientist_agent import MLScientistAgent
from agentplatform.infrastructure.registration.tool_registration import (
    register_default_tools,
)
from agentplatform.infrastructure.tools.experiment_executor_adapter import (
    ExperimentExecutorAdapter,
)


class LegacyExperimentExecutor(ToolContract):
    """Replica of the pre-fix adapter that raised on missing command."""

    @property
    def tool_type(self) -> ToolType:
        return ToolType.EXPERIMENT_EXECUTOR

    def execute(self, payload: dict[str, object]) -> dict[str, object]:
        command = str(payload.get("command", ""))
        if not command:
            raise ValueError("Experiment command required.")
        return {"success": True, "command": command, "legacy": True}


class RecordingExecutor:
    def __init__(self) -> None:
        self.calls: list[tuple[ToolType, dict[str, object]]] = []

    def execute(
        self,
        tool_type: ToolType,
        payload: dict[str, object],
    ) -> dict[str, object]:
        self.calls.append((tool_type, payload))
        if tool_type in {ToolType.EXPERIMENT_DESIGN, ToolType.EXPERIMENT_EXECUTOR}:
            if not str(payload.get("command", "")).strip():
                raise ValueError("Experiment command required.")
        return {"success": True, "tool": tool_type.value, "payload": payload}


def _context(tmp_path: Path) -> AgentExecutionContext:
    project = Project(
        name="demo",
        path=tmp_path,
        project_type="software",
    )
    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Evaluate baseline model",
        target_project=project,
    )


def test_experiment_executor_adapter_does_not_require_command() -> None:
    result = ExperimentExecutorAdapter().execute({"path": "/tmp/project"})
    assert result["success"] is True
    assert "Experiment command required" not in str(result)


def test_ml_scientist_passes_command_to_legacy_executor(tmp_path: Path) -> None:
    executor = RecordingExecutor()
    agent = MLScientistAgent(tool_executor=executor)
    result = agent.run(_context(tmp_path))

    assert result.success is True
    assert result.message != "Experiment command required."
    design_calls = [
        payload
        for tool_type, payload in executor.calls
        if tool_type == ToolType.EXPERIMENT_DESIGN
    ]
    assert design_calls
    assert str(design_calls[0].get("command", "")).strip()


def test_tool_executor_retries_legacy_experiment_command_error() -> None:
    registry = ToolRegistry()
    registry.register(
        ToolDefinition(
            name="experiment_executor",
            tool_type=ToolType.EXPERIMENT_DESIGN,
            description="legacy mapping",
        ),
        LegacyExperimentExecutor(),
    )
    executor = ToolExecutor(registry)
    result = executor.execute(ToolType.EXPERIMENT_DESIGN, {"path": "."})
    assert result["success"] is True
    assert result["command"]


def test_ml_scientist_with_default_tool_registration(tmp_path: Path) -> None:
    registry = register_default_tools(ToolRegistry())
    agent = MLScientistAgent(tool_executor=ToolExecutor(registry))
    result = agent.run(_context(tmp_path))
    assert result.success is True
    assert result.data["agent"] == "ml_scientist"
    assert result.data["evaluation"]["model_name"] == "baseline"
