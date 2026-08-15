"""
ShadBot Agent Platform

Regression tests for run-3 defects.

  BUG P - the model echoed the source root back into import statements
          ("from src.agentplatform.domain... import X"), so 5 of 10 generated
          modules raised ModuleNotFoundError.

  BUG Q - the model answered a request for file A with content labelled as
          file B, so the planned module was never written and every dependent
          import broke. Run 3 lost domain/agents/agent_role.py this way.

  BUG R - circular imports were reported as "cannot import name X", sending
          the reader hunting for a symbol that is actually present.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from agentplatform.application.generation import (
    CodeGenerationService,
    ModuleSplitter,
)
from agentplatform.application.prompt.prompt_builder import (
    CODEGEN_FILE_KEY,
    CODEGEN_PURPOSE_KEY,
    CODEGEN_SIBLINGS_KEY,
    PromptBuilder,
)
from agentplatform.application.quality_gate import ImportValidator
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext


# ---------------------------------------------------------------------------
# BUG P - source root leaking into imports
# ---------------------------------------------------------------------------


def test_strip_source_root_imports_rewrites_from_imports() -> None:
    code = (
        "from src.agentplatform.domain.agents.agent_role import AgentRole\n"
        "from src.agentplatform.application.release.release_service import R\n"
    )

    fixed = ModuleSplitter.strip_source_root_imports(code)

    assert "from src." not in fixed
    assert "from agentplatform.domain.agents.agent_role import AgentRole" in fixed


def test_strip_source_root_imports_rewrites_plain_imports() -> None:
    fixed = ModuleSplitter.strip_source_root_imports(
        "import src.agentplatform.domain.models\n",
    )

    assert fixed.strip() == "import agentplatform.domain.models"


def test_strip_source_root_imports_leaves_legitimate_names() -> None:
    """
    A package genuinely called `source_control` must not be mangled.
    """

    code = (
        "from source_control import Repo\n"
        "from srcutils import helper\n"
        "import sources\n"
    )

    assert ModuleSplitter.strip_source_root_imports(code) == code


def test_splitter_applies_import_repair() -> None:
    code = (
        "# src/pkg/a.py\n"
        "from src.pkg.b import Thing\n"
        "\n"
        "# src/pkg/b.py\n"
        "class Thing:\n"
        "    pass\n"
    )

    modules = ModuleSplitter().split(code, default_path="src/pkg/a.py")

    joined = "\n".join(m.content for m in modules)

    assert "from src.pkg" not in joined
    assert "from pkg.b import Thing" in joined


def test_prompt_states_the_dotted_import_path() -> None:
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="x",
        task_title="T",
        metadata={
            CODEGEN_FILE_KEY: "src/agentplatform/domain/models.py",
            CODEGEN_PURPOSE_KEY: "Entities",
            CODEGEN_SIBLINGS_KEY: ["src/agentplatform/domain/agents.py"],
        },
    )

    prompt = PromptBuilder().build(AgentRole.ENGINEER, context)

    assert "agentplatform.domain.models" in prompt
    assert "- agentplatform.domain.agents" in prompt
    assert "never write" in prompt.lower()


def test_prompt_forbids_circular_imports() -> None:
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="x",
        task_title="T",
        metadata={
            CODEGEN_FILE_KEY: "src/pkg/mod.py",
            CODEGEN_PURPOSE_KEY: "Something",
        },
    )

    prompt = PromptBuilder().build(AgentRole.ENGINEER, context)

    assert "circular import" in prompt.lower()


# ---------------------------------------------------------------------------
# BUG Q - planned module never written
# ---------------------------------------------------------------------------


class _MisdirectingBrain:
    """Answers a request for file A with content labelled as file B."""

    def think(self, role: object, context: object) -> str:
        return (
            "```python\n"
            "# src/pkg/other.py\n"
            "from enum import Enum\n"
            "\n"
            "class AgentRole(Enum):\n"
            '    """Roles."""\n'
            '    ENGINEER = "Engineer"\n'
            "```"
        )


def test_missing_planned_module_gets_a_reexport_shim(tmp_path: Path) -> None:
    """
    The run-3 failure: AgentRole landed in agent_contract.py, agent_role.py
    was never written, and 5 modules failed to import it.
    """

    service = CodeGenerationService(
        brain=_MisdirectingBrain(),
        project_root=tmp_path,
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="x",
        task_title="T",
        metadata={},
    )

    service.generate(
        context=context,
        file_path=tmp_path / "src/pkg/agent_role.py",
        instructions="x",
        purpose="Agent role enumeration",
    )

    planned = tmp_path / "src/pkg/agent_role.py"

    assert planned.exists(), "planned module must always be created"

    content = planned.read_text(encoding="utf-8")

    assert "from pkg.other import AgentRole" in content
    assert "src." not in content


def test_shim_makes_the_project_importable(tmp_path: Path) -> None:
    service = CodeGenerationService(
        brain=_MisdirectingBrain(),
        project_root=tmp_path,
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="x",
        task_title="T",
        metadata={},
    )

    service.generate(
        context=context,
        file_path=tmp_path / "src/pkg/agent_role.py",
        instructions="x",
        purpose="Agent role enumeration",
    )

    result = ImportValidator().validate(str(tmp_path))

    assert result.passed is True


class _SilentBrain:
    def think(self, role: object, context: object) -> str:
        return "```python\n# src/pkg/unrelated.py\nX = 1\n```"


def test_shim_raises_when_nothing_matches(tmp_path: Path) -> None:
    """
    No matching symbol means an honest NotImplementedError, never a silent
    empty module that would let the gate pass.
    """

    service = CodeGenerationService(
        brain=_SilentBrain(),
        project_root=tmp_path,
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="x",
        task_title="T",
        metadata={},
    )

    service.generate(
        context=context,
        file_path=tmp_path / "src/pkg/missing_thing.py",
        instructions="x",
        purpose="Something",
    )

    content = (tmp_path / "src/pkg/missing_thing.py").read_text(encoding="utf-8")

    assert "NotImplementedError" in content


# ---------------------------------------------------------------------------
# BUG R - circular import diagnosis
# ---------------------------------------------------------------------------


def test_circular_import_is_named_as_such(tmp_path: Path) -> None:
    pkg = tmp_path / "src" / "pkg"
    pkg.mkdir(parents=True)

    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "a.py").write_text(
        "from pkg.b import B\n\n\nclass A:\n    pass\n",
        encoding="utf-8",
    )
    (pkg / "b.py").write_text(
        "from pkg.a import A\n\n\nclass B:\n    pass\n",
        encoding="utf-8",
    )

    result = ImportValidator().validate(str(tmp_path))

    assert result.passed is False
    assert "CIRCULAR IMPORT" in result.details
