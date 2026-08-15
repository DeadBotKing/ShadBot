"""
ShadBot Agent Platform

Regression tests for the three defects found auditing ShadBotCore_BuiltByAgent:

  BUG I  - the deterministic gate validated the ShadBot platform itself
           instead of the generated project, because it fell back to Path(".")
           whenever the target could not be resolved.

  BUG J  - multi-module LLM responses were written verbatim into one file,
           producing parseable but unimportable code.

  BUG K  - the gate had no import check, so 14 files of which 0 could be
           imported were reported as [PASS] syntax.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

import pytest

from agentplatform.application.generation import ModuleSplitter
from agentplatform.application.orchestration.agent_orchestrator import (
    AgentOrchestrator,
)
from agentplatform.application.quality_gate import ImportValidator
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.workspace import Project


def _context(
    project_path: Path | None,
    metadata: dict[str, object] | None = None,
) -> AgentExecutionContext:
    project = (
        Project(
            name="target",
            path=project_path,
            project_type="software",
        )
        if project_path is not None
        else None
    )

    return AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="test",
        target_project=project,
        metadata=metadata or {},
    )


# ---------------------------------------------------------------------------
# BUG I - gate target resolution
# ---------------------------------------------------------------------------


def test_gate_target_uses_target_project_path(tmp_path: Path) -> None:
    project = tmp_path / "GeneratedProject"
    project.mkdir()

    resolved = AgentOrchestrator._resolve_target_project_path(
        _context(project),
    )

    assert resolved == project.resolve()


def test_gate_target_never_falls_back_to_cwd() -> None:
    """
    The defect: an unresolvable target silently became Path("."), so the gate
    validated ShadBot's own source tree and reported the platform's 23
    architecture violations as if the agent had produced them.
    """

    with pytest.raises(ValueError, match="Cannot determine the target project"):
        AgentOrchestrator._resolve_target_project_path(_context(None))


def test_gate_target_rejects_nonexistent_path(tmp_path: Path) -> None:
    missing = tmp_path / "does-not-exist"

    with pytest.raises(ValueError):
        AgentOrchestrator._resolve_target_project_path(_context(missing))


def test_gate_target_falls_back_to_metadata(tmp_path: Path) -> None:
    project = tmp_path / "FromMetadata"
    project.mkdir()

    resolved = AgentOrchestrator._resolve_target_project_path(
        _context(None, {"project_path": str(project)}),
    )

    assert resolved == project.resolve()


def test_gate_target_rejects_file_target(tmp_path: Path) -> None:
    a_file = tmp_path / "not_a_dir.py"
    a_file.write_text("x = 1\n", encoding="utf-8")

    with pytest.raises(ValueError):
        AgentOrchestrator._resolve_target_project_path(_context(a_file))


# ---------------------------------------------------------------------------
# BUG J - multi-module splitting
# ---------------------------------------------------------------------------


CONCATENATED = '''# src/agentplatform/domain/models.py

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Agent:
    name: str

# src/agentplatform/domain/services.py

from .models import Agent

class DomainService:
    def all_agents(self) -> List[Agent]:
        return []
'''


def test_splitter_separates_concatenated_modules() -> None:
    modules = ModuleSplitter().split(
        CONCATENATED,
        default_path="src/agentplatform/domain/agent_role.py",
    )

    paths = [m.path for m in modules]

    assert paths == [
        "src/agentplatform/domain/models.py",
        "src/agentplatform/domain/services.py",
    ]
    assert all(m.is_parseable for m in modules)


def test_splitter_propagates_shared_stdlib_imports() -> None:
    """
    `List` is imported once at the top and used in a later module. After
    splitting, that module must still import it or it raises NameError.
    """

    modules = ModuleSplitter().split(CONCATENATED, default_path="x.py")

    services = next(m for m in modules if m.path.endswith("services.py"))

    assert "from typing import List" in services.content


def test_splitter_never_propagates_relative_imports() -> None:
    modules = ModuleSplitter().split(CONCATENATED, default_path="x.py")

    models = next(m for m in modules if m.path.endswith("models.py"))

    assert "from .models import" not in models.content


def test_splitter_returns_single_module_when_no_delimiters() -> None:
    modules = ModuleSplitter().split(
        "def f() -> int:\n    return 1\n",
        default_path="src/pkg/mod.py",
    )

    assert len(modules) == 1
    assert modules[0].path == "src/pkg/mod.py"


def test_splitter_rejects_path_traversal() -> None:
    hostile = "# ../../../etc/evil.py\nx = 1\n"

    modules = ModuleSplitter().split(hostile, default_path="safe.py")

    assert all(".." not in m.path for m in modules)


def test_splitter_merges_duplicate_paths() -> None:
    duplicated = (
        "# src/a.py\nx = 1\n\n"
        "# src/b.py\ny = 2\n\n"
        "# src/a.py\nz = 3\n"
    )

    modules = ModuleSplitter().split(duplicated, default_path="d.py")

    paths = [m.path for m in modules]

    assert paths.count("src/a.py") == 1

    merged = next(m for m in modules if m.path == "src/a.py")

    assert "x = 1" in merged.content
    assert "z = 3" in merged.content


# ---------------------------------------------------------------------------
# BUG K - import validation
# ---------------------------------------------------------------------------


def test_import_validator_fails_parseable_but_unimportable_code(
    tmp_path: Path,
) -> None:
    """
    The exact ShadBotCore_BuiltByAgent failure: valid syntax, dead imports.
    """

    src = tmp_path / "src" / "pkg"
    src.mkdir(parents=True)
    (src / "__init__.py").write_text("", encoding="utf-8")
    (src / "service.py").write_text(
        "from .models import Agent\n\n\nclass Service:\n    pass\n",
        encoding="utf-8",
    )

    result = ImportValidator().validate(str(tmp_path))

    assert result.passed is False
    assert result.skipped is False
    assert "cannot be imported" in result.details


def test_import_validator_passes_working_code(tmp_path: Path) -> None:
    src = tmp_path / "src" / "pkg"
    src.mkdir(parents=True)
    (src / "__init__.py").write_text("", encoding="utf-8")
    (src / "models.py").write_text(
        "class Agent:\n    pass\n",
        encoding="utf-8",
    )
    (src / "service.py").write_text(
        "from pkg.models import Agent\n\n\nclass Service:\n    agent = Agent\n",
        encoding="utf-8",
    )

    result = ImportValidator().validate(str(tmp_path))

    assert result.passed is True
    assert result.score == 1.0


def test_import_validator_skips_empty_project(tmp_path: Path) -> None:
    result = ImportValidator().validate(str(tmp_path))

    assert result.skipped is True
    assert result.passed is False


def test_import_validator_reports_line_numbers(tmp_path: Path) -> None:
    src = tmp_path / "src"
    src.mkdir()
    (src / "broken.py").write_text(
        "import os\n\nraise RuntimeError('boom')\n",
        encoding="utf-8",
    )

    result = ImportValidator().validate(str(tmp_path))

    assert result.passed is False
    assert "broken.py:3" in result.details


def test_import_check_is_part_of_the_gate() -> None:
    from agentplatform.application.quality_gate import DeterministicQualityGate

    gate = DeterministicQualityGate()

    assert hasattr(gate, "import_val")
