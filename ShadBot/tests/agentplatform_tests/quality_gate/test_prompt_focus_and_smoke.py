"""
ShadBot Agent Platform

Regression tests for the run-2 defects.

  BUG L - the gate reported GREEN on code that crashed at runtime, because
          importing a module never executes main().

  BUG M - per-file codegen prompts were 96.4% identical, so the model returned
          the same response for 11 different modules.

  BUG N - identical prompts were re-sent to the model instead of cached.

  BUG O - the generated run.py printed "operational" without importing
          anything, so it exited 0 on a completely broken project.
"""

from __future__ import annotations

import difflib
import re
from pathlib import Path
from uuid import uuid4

from agentplatform.application.prompt.prompt_builder import (
    CODEGEN_FILE_KEY,
    CODEGEN_PURPOSE_KEY,
    CODEGEN_SIBLINGS_KEY,
    PromptBuilder,
)
from agentplatform.application.quality_gate import SmokeRunValidator
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext

LONG_TASK_DESCRIPTION = (
    "Implement the complete ShadBot Agent Platform in 'src/agentplatform/' "
    "from Phase 1 through Phase 12. " * 6
)


def _codegen_context(
    target: str,
    purpose: str,
) -> AgentExecutionContext:
    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Implement the module.",
        task_title="Autonomous Implementation of ShadBot Agent Platform",
        task_description=LONG_TASK_DESCRIPTION,
        task_type="full_lifecycle",
        metadata={
            CODEGEN_FILE_KEY: target,
            CODEGEN_PURPOSE_KEY: purpose,
            CODEGEN_SIBLINGS_KEY: [
                "src/agentplatform/domain/agents/agent_role.py",
                "src/agentplatform/application/release/release_service.py",
            ],
        },
    )


# ---------------------------------------------------------------------------
# BUG M - prompt differentiation
# ---------------------------------------------------------------------------


def test_codegen_prompts_for_different_files_are_distinct() -> None:
    """
    The defect: two prompts for completely different modules were 96.4%
    identical, differing only in one buried Instructions line.
    """

    builder = PromptBuilder()

    a = builder.build(
        AgentRole.ENGINEER,
        _codegen_context(
            "src/agentplatform/domain/agents/agent_role.py",
            "Agent identity and role enumeration (Phase 2)",
        ),
    )
    b = builder.build(
        AgentRole.ENGINEER,
        _codegen_context(
            "src/agentplatform/application/release/release_service.py",
            "Production Freeze V1.0 and SLA governance (Phase 12)",
        ),
    )

    similarity = difflib.SequenceMatcher(None, a, b).ratio()

    assert similarity < 0.90, f"prompts are {similarity:.1%} similar"

    # The opening of the prompt - what the model weighs most - must differ.
    assert a[:150] != b[:150]


def test_codegen_prompt_omits_the_full_task_description() -> None:
    """
    The huge shared task description is what made every prompt look alike.
    """

    prompt = PromptBuilder().build(
        AgentRole.ENGINEER,
        _codegen_context("src/pkg/mod.py", "Do one thing"),
    )

    assert LONG_TASK_DESCRIPTION not in prompt


def test_codegen_prompt_names_the_target_file_first() -> None:
    prompt = PromptBuilder().build(
        AgentRole.ENGINEER,
        _codegen_context("src/agentplatform/domain/models.py", "Entities"),
    )

    assert prompt.startswith("Write ONE Python file: models.py")
    assert "src/agentplatform/domain/models.py" in prompt


def test_codegen_prompt_forbids_multi_module_output() -> None:
    """
    Without this instruction the model emits several modules per response.
    """

    prompt = PromptBuilder().build(
        AgentRole.ENGINEER,
        _codegen_context("src/pkg/mod.py", "Do one thing"),
    )

    assert "Do NOT write other modules" in prompt
    assert "section headers" in prompt


def test_codegen_prompt_carries_layer_rules() -> None:
    builder = PromptBuilder()

    domain = builder.build(
        AgentRole.ENGINEER,
        _codegen_context("src/agentplatform/domain/models.py", "Entities"),
    )
    infra = builder.build(
        AgentRole.ENGINEER,
        _codegen_context(
            "src/agentplatform/infrastructure/tools/git_tool.py",
            "Git adapter",
        ),
    )

    assert "LAYER: DOMAIN" in domain
    assert "frozen=True" in domain

    assert "LAYER: INFRASTRUCTURE" in infra
    assert "shell=True" in infra


def test_general_prompt_still_used_without_codegen_target() -> None:
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Research the topic.",
        task_title="Research",
        task_description=LONG_TASK_DESCRIPTION,
        metadata={},
    )

    prompt = PromptBuilder().build(AgentRole.RESEARCHER, context)

    assert "You are an AI software engineering agent." in prompt


# ---------------------------------------------------------------------------
# BUG L - smoke run
# ---------------------------------------------------------------------------


def _make_project(tmp_path: Path, service_body: str) -> Path:
    pkg = tmp_path / "src" / "app"
    pkg.mkdir(parents=True)

    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "domain.py").write_text(
        "class Domain:\n"
        "    def __init__(self, data):\n"
        "        self._data = data\n\n"
        "    @property\n"
        "    def data(self):\n"
        "        return self._data\n",
        encoding="utf-8",
    )
    (pkg / "service.py").write_text(service_body, encoding="utf-8")
    (pkg / "__main__.py").write_text(
        "from .domain import Domain\n"
        "from .service import Service\n\n"
        "def main():\n"
        "    print(Service(Domain({'k': 'v'})).run())\n\n"
        'if __name__ == "__main__":\n'
        "    main()\n",
        encoding="utf-8",
    )

    return tmp_path


BROKEN_SERVICE = (
    "class Service:\n"
    "    def __init__(self, domain):\n"
    "        self.domain = domain\n\n"
    "    def run(self):\n"
    "        return self.domain.data('x')\n"  # property called like a function
)

WORKING_SERVICE = (
    "class Service:\n"
    "    def __init__(self, domain):\n"
    "        self.domain = domain\n\n"
    "    def run(self):\n"
    "        return self.domain.data\n"
)


def test_smoke_run_catches_runtime_crash_that_imports_cleanly(
    tmp_path: Path,
) -> None:
    """
    The exact run-2 failure: every module imports, the gate said GREEN, and
    `python -m app` died with TypeError: 'dict' object is not callable.
    """

    project = _make_project(tmp_path, BROKEN_SERVICE)

    result = SmokeRunValidator().validate(str(project))

    assert result.passed is False
    assert result.skipped is False
    assert "TypeError" in result.details


def test_smoke_run_reports_file_and_line(tmp_path: Path) -> None:
    project = _make_project(tmp_path, BROKEN_SERVICE)

    result = SmokeRunValidator().validate(str(project))

    assert re.search(r"service\.py:\d+", result.details)


def test_smoke_run_passes_working_project(tmp_path: Path) -> None:
    project = _make_project(tmp_path, WORKING_SERVICE)

    result = SmokeRunValidator().validate(str(project))

    assert result.passed is True
    assert result.score == 1.0


def test_smoke_run_fails_on_nonzero_exit(tmp_path: Path) -> None:
    (tmp_path / "run.py").write_text(
        "import sys\nsys.exit(3)\n",
        encoding="utf-8",
    )

    result = SmokeRunValidator().validate(str(tmp_path))

    assert result.passed is False
    assert "code 3" in result.details


def test_smoke_run_skips_project_without_entry_point(tmp_path: Path) -> None:
    src = tmp_path / "src"
    src.mkdir()
    (src / "lib.py").write_text("x = 1\n", encoding="utf-8")

    result = SmokeRunValidator().validate(str(tmp_path))

    assert result.skipped is True
    assert result.passed is False


def test_smoke_run_is_part_of_the_gate() -> None:
    from agentplatform.application.quality_gate import DeterministicQualityGate

    assert hasattr(DeterministicQualityGate(), "smoke_val")


# ---------------------------------------------------------------------------
# BUG N - prompt cache
# ---------------------------------------------------------------------------


def test_llm_cache_returns_identical_response_without_second_call() -> None:
    from agentplatform.infrastructure.llm.ollama_provider import OllamaProvider

    provider = OllamaProvider()

    calls: list[str] = []

    def fake_post(*args: object, **kwargs: object) -> object:
        calls.append("call")

        class _Response:
            @staticmethod
            def raise_for_status() -> None:
                return None

            @staticmethod
            def json() -> dict[str, str]:
                return {"response": "generated code"}

        return _Response()

    provider._is_available = lambda endpoint: True  # type: ignore[method-assign]

    import agentplatform.infrastructure.llm.ollama_provider as module

    original_post = module.requests.post
    module.requests.post = fake_post  # type: ignore[assignment]

    try:
        first = provider.generate("identical prompt")
        second = provider.generate("identical prompt")
        third = provider.generate("a different prompt")
    finally:
        module.requests.post = original_post  # type: ignore[assignment]

    assert first == second == "generated code"
    assert len(calls) == 2, "identical prompt must not be re-sent"
    assert provider.cache_hits == 1
    assert third == "generated code"


def test_llm_cache_can_be_disabled(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    from agentplatform.infrastructure.llm.ollama_provider import OllamaProvider

    monkeypatch.setenv("SHADBOT_LLM_CACHE", "0")

    assert OllamaProvider()._cache_enabled is False


# ---------------------------------------------------------------------------
# BUG O - the generated runner must exercise the code
# ---------------------------------------------------------------------------


def test_generated_runner_template_imports_modules() -> None:
    """
    The old template printed "operational" without importing anything, so it
    exited 0 even when every generated module was broken.
    """

    source = Path(
        "src/agentplatform/infrastructure/agents/engineer_agent.py"
    ).read_text(encoding="utf-8")

    match = re.search(r"run_content = \(\n(.*?)\n\s*\)\n", source, re.DOTALL)

    assert match is not None, "run.py template not found"

    template = match.group(1)

    assert "importlib" in template
    assert "pkgutil" in template
    assert "return 1" in template, "must signal failure with a non-zero exit"
