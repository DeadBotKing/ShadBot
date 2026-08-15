"""
ShadBot Agent Platform

Engineer Agent tests.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from agentplatform.domain.architecture_plan import ArchitecturePlan, FilePlan
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.infrastructure.agents.engineer_agent import EngineerAgent


class FakeArtifact:
    def __init__(self, path: Path) -> None:
        self.path = path


class FakeCodeGenerationService:
    def generate(self, context, file_path, instructions):
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("# Autonomously generated code\n", encoding="utf-8")
        return FakeArtifact(file_path)


class FakeToolExecutor:
    def execute(self, tool_type, payload):
        return {"status": "SUCCESS"}


def test_engineer_agent_execution_and_run_script_generation(tmp_path: Path) -> None:
    code_srv = FakeCodeGenerationService()
    tool_exec = FakeToolExecutor()
    agent = EngineerAgent(code_generation_service=code_srv, tool_executor=tool_exec)

    file_plan = FilePlan(path="src/indicators/market_analyzer.py", action="create", purpose="MACD indicator")
    plan = ArchitecturePlan(
        plan_id=uuid4(),
        task_id=uuid4(),
        summary="Architecture approved",
        file_plan=(file_plan,),
        dependency_plan=(),
        interface_plan=(),
        implementation_order=(),
        acceptance_criteria=(),
    )

    class FakeProject:
        path = tmp_path

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Implement module",
        task_title="MACD feature",
        metadata={"architecture_plan": plan},
        target_project=FakeProject(),  # type: ignore[arg-type]
    )

    res = agent.run(context)
    assert res.success is True
    assert "run.py" in str(res.data["generated_files"])
    run_script = tmp_path / "run.py"
    assert run_script.exists()
    assert "ShadBot Autonomously Generated Runner" in run_script.read_text(encoding="utf-8")
