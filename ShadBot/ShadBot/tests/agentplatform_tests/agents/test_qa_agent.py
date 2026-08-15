"""
ShadBot Agent Platform

QA agent and quality-validator contract tests.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.tools import ToolType
from agentplatform.domain.workspace import Project
from agentplatform.infrastructure.agents.qa_agent import QAAgent
from agentplatform.infrastructure.tools.quality_validator import QualityValidator
from agentplatform.infrastructure.tools.terminal_tool import TerminalTool


class ExplodingQualityExecutor:
    def execute(self, tool_type: ToolType, payload: dict[str, object]) -> dict[str, object]:
        if tool_type == ToolType.QUALITY_VALIDATOR:
            raise RuntimeError("")
        return {"success": True, "tool": tool_type.value, "payload": payload}


class RecordingExecutor:
    def execute(self, tool_type: ToolType, payload: dict[str, object]) -> dict[str, object]:
        return {"success": True, "status": "PASS", "tool": tool_type.value}


def _context(tmp_path: Path) -> AgentExecutionContext:
    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Validate quality",
        target_project=Project(name="demo", path=tmp_path, project_type="software"),
    )


def test_qa_survives_empty_runtime_error(tmp_path: Path) -> None:
    agent = QAAgent(tool_executor=ExplodingQualityExecutor())  # type: ignore[arg-type]
    result = agent.run(_context(tmp_path))
    assert result.success is True
    assert result.message != ""
    assert result.data["validation"]["error_type"] == "RuntimeError"


def test_qa_completes_with_healthy_tools(tmp_path: Path) -> None:
    agent = QAAgent(tool_executor=RecordingExecutor())  # type: ignore[arg-type]
    result = agent.run(_context(tmp_path))
    assert result.success is True
    assert result.data["agent"] == "qa"
    assert result.data["findings"] is False


def test_quality_validator_does_not_raise_on_failing_command(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)

    class FakeCompleted:
        returncode = 1
        stdout = "ruff found issues"
        stderr = ""

    monkeypatch.setattr(
        "agentplatform.infrastructure.tools.quality_validator.subprocess.run",
        lambda *args, **kwargs: FakeCompleted(),
    )
    report = QualityValidator().validate(tmp_path)
    assert report["status"] == "FAIL"
    assert report["success"] is False
    assert "ruff found issues" in str(report["checks"]["ruff"]["output"])


def test_terminal_tool_includes_stdout_when_stderr_empty(
    monkeypatch,
    tmp_path: Path,
) -> None:
    class FakeCompleted:
        returncode = 1
        stdout = "lint errors on stdout"
        stderr = ""

    monkeypatch.setattr(
        "agentplatform.infrastructure.tools.terminal_tool.subprocess.run",
        lambda *args, **kwargs: FakeCompleted(),
    )
    try:
        TerminalTool().execute("ruff check .", str(tmp_path))
        raise AssertionError("expected RuntimeError")
    except RuntimeError as exc:
        assert str(exc) == "lint errors on stdout"
