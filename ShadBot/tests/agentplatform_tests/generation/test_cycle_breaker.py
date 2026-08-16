"""
ShadBot Agent Platform

Regression tests for BUG R: import cycles in generated projects.

Run 4 of ShadBotCore_BuiltByAgent failed 6 of 11 import checks from a single
cause: `AgentOrchestrator` imported four application services, and all four
imported `AgentOrchestrator` back for type annotations only.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from agentplatform.application.generation import ImportCycleBreaker


def _write(root: Path, relative: str, body: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


def _make_package(root: Path, *modules: str) -> None:
    for module in modules:
        directory = root / module
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "__init__.py").write_text("", encoding="utf-8")


def _import_all(root: Path, modules: list[str]) -> list[str]:
    """
    Import each module in a fresh interpreter. Returns the failures.
    """

    failures: list[str] = []

    for module in modules:
        result = subprocess.run(
            [sys.executable, "-c", f"import {module}"],
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={"PYTHONPATH": str(root)},
        )

        if result.returncode != 0:
            failures.append(module)

    return failures


class TestAnnotationOnlyCycle:
    """
    The run-4 failure shape: mutual imports used only in type hints.
    """

    @pytest.fixture()
    def project(self, tmp_path: Path) -> Path:
        root = tmp_path / "src"
        _make_package(root, "app", "app/orchestration", "app/platform")

        _write(
            root,
            "app/orchestration/orchestrator.py",
            "from app.platform.platform_service import PlatformService\n"
            "\n"
            "class Orchestrator:\n"
            "    def __init__(self, service: PlatformService) -> None:\n"
            "        self._service = service\n",
        )

        _write(
            root,
            "app/platform/platform_service.py",
            "from app.orchestration.orchestrator import Orchestrator\n"
            "\n"
            "class PlatformService:\n"
            "    def __init__(self, orchestrator: Orchestrator) -> None:\n"
            "        self._orchestrator = orchestrator\n",
        )

        return root

    def test_cycle_is_broken(self, project: Path) -> None:
        repairs, unrepaired = ImportCycleBreaker(project).repair()

        assert repairs, "the cycle should have been repaired"
        assert unrepaired == []

    def test_modules_import_after_repair(self, project: Path) -> None:
        modules = [
            "app.orchestration.orchestrator",
            "app.platform.platform_service",
        ]

        assert _import_all(project, modules), "fixture must start broken"

        ImportCycleBreaker(project).repair()

        assert _import_all(project, modules) == []

    def test_type_checking_guard_is_added(self, project: Path) -> None:
        """
        Breaking either edge resolves the cycle, so assert on the file the
        repair actually chose rather than a hard-coded one.
        """

        repairs, _ = ImportCycleBreaker(project).repair()

        assert len(repairs) == 1, "one edge is enough to break a 2-node cycle"

        repaired = project / (repairs[0].module.replace(".", "/") + ".py")

        rewritten = repaired.read_text(encoding="utf-8")

        assert "if TYPE_CHECKING:" in rewritten
        assert "from __future__ import annotations" in rewritten

    def test_repair_is_idempotent(self, project: Path) -> None:
        ImportCycleBreaker(project).repair()

        second, _ = ImportCycleBreaker(project).repair()

        assert second == []


class TestRuntimeCycleIsReported:
    """
    A cycle whose imports really execute must NOT be silently rewritten.
    """

    def test_runtime_cycle_is_left_alone(self, tmp_path: Path) -> None:
        root = tmp_path / "src"
        _make_package(root, "app")

        _write(
            root,
            "app/left.py",
            "from app.right import RIGHT\n\nLEFT = RIGHT + 1\n",
        )
        _write(
            root,
            "app/right.py",
            "from app.left import LEFT\n\nRIGHT = LEFT + 1\n",
        )

        repairs, unrepaired = ImportCycleBreaker(root).repair()

        assert repairs == []
        assert unrepaired, "a runtime cycle must be reported, not hidden"


class TestMainGuard:
    """
    Names used inside `if __name__ == "__main__":` do not run at import time.
    """

    def test_main_block_keeps_working(self, tmp_path: Path) -> None:
        root = tmp_path / "src"
        _make_package(root, "app")

        _write(
            root,
            "app/service.py",
            "from app.engine import Engine\n"
            "\n"
            "class Service:\n"
            "    def __init__(self, engine: Engine) -> None:\n"
            "        self._engine = engine\n"
            "\n"
            'if __name__ == "__main__":\n'
            "    engine = Engine()\n"
            "    print(Service(engine))\n",
        )

        _write(
            root,
            "app/engine.py",
            "from app.service import Service\n"
            "\n"
            "class Engine:\n"
            "    def run(self, service: Service) -> None:\n"
            "        self._service = service\n",
        )

        repairs, unrepaired = ImportCycleBreaker(root).repair()

        assert repairs
        assert unrepaired == []

        # Whichever edge was broken, the __main__ demo must still be able to
        # construct the class it references.
        modules = ["app.service", "app.engine"]

        assert _import_all(root, modules) == []

        script = subprocess.run(
            [sys.executable, str(root / "app" / "service.py")],
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={"PYTHONPATH": str(root)},
        )

        assert script.returncode == 0, script.stderr

    def test_type_checking_block_is_not_nested_in_main(
        self,
        tmp_path: Path,
    ) -> None:
        """
        The TYPE_CHECKING block must sit at module level, never inside the
        __main__ guard - that bug made the repair a no-op at import time.
        """

        root = tmp_path / "src"
        _make_package(root, "app")

        _write(
            root,
            "app/service.py",
            "from app.engine import Engine\n"
            "\n"
            "class Service:\n"
            "    def __init__(self, engine: Engine) -> None:\n"
            "        self._engine = engine\n"
            "\n"
            'if __name__ == "__main__":\n'
            "    engine = Engine()\n",
        )
        _write(
            root,
            "app/engine.py",
            "from app.service import Service\n"
            "\n"
            "class Engine:\n"
            "    def run(self, service: Service) -> None:\n"
            "        self._service = service\n",
        )

        ImportCycleBreaker(root).repair()

        for name in ("service.py", "engine.py"):
            text = (root / "app" / name).read_text(encoding="utf-8")

            for line in text.splitlines():
                if line.strip() == "if TYPE_CHECKING:":
                    assert not line.startswith(" "), (
                        f"{name}: TYPE_CHECKING block is indented, so it is "
                        "nested inside another block and never applies"
                    )


class TestNoCycle:
    """
    A clean project must be left untouched.
    """

    def test_acyclic_project_is_unchanged(self, tmp_path: Path) -> None:
        root = tmp_path / "src"
        _make_package(root, "app")

        original = "VALUE = 1\n"
        path = _write(root, "app/settings.py", original)

        repairs, unrepaired = ImportCycleBreaker(root).repair()

        assert repairs == []
        assert unrepaired == []
        assert path.read_text(encoding="utf-8") == original
