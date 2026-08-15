"""
ShadBot Agent Platform

Validation check components for Phase 9 Quality Gate System.

Purpose:
    Execute REAL deterministic quality tooling against a target project and
    report truthful PASS/FAIL results.

Responsibility:
    Each validator owns exactly one external quality tool (or one static
    analysis rule set) and converts its process outcome into a CheckResult.

Dependencies:
    Standard library only (subprocess, shutil, ast, pathlib).

Outputs:
    CheckResult instances carrying passed/details/score.

Design rules honoured:
    - Rule 27: no fake implementations. A validator NEVER returns a hardcoded
      pass. If a tool is unavailable the result is reported as SKIPPED with an
      explicit reason, and skipped checks are excluded from scoring by the
      service layer instead of silently counting as success.
    - Rule 18: no bare excepts, failures are reported not swallowed.
"""

from __future__ import annotations

import ast
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

# Recursion guard: a nested pytest invocation from inside a pytest process
# forks indefinitely. When running under pytest we must never spawn pytest.
_PYTEST_ENV_MARKER = "PYTEST_CURRENT_TEST"

# Hard wall-clock ceiling for any external quality tool.
_DEFAULT_TOOL_TIMEOUT_SECONDS = int(
    os.getenv(
        "SHADBOT_QUALITY_TOOL_TIMEOUT",
        "300",
    )
)

_MAX_DETAIL_CHARS = 4000


@dataclass(frozen=True, slots=True)
class CheckResult:
    """
    Outcome of a single quality check.

    skipped=True means the check could not be executed (missing tool, nested
    pytest, absent target). A skipped check is NOT a pass and must not be
    counted as evidence of quality.
    """

    check_name: str
    passed: bool
    details: str
    score: float
    skipped: bool = False

    def to_dict(self) -> dict[str, object]:
        return {
            "check_name": self.check_name,
            "passed": self.passed,
            "details": self.details,
            "score": self.score,
            "skipped": self.skipped,
        }


def _truncate(text: str) -> str:
    cleaned = text.strip()

    if len(cleaned) <= _MAX_DETAIL_CHARS:
        return cleaned

    return cleaned[:_MAX_DETAIL_CHARS] + "\n... [output truncated]"


def _combine_output(
    stdout: str | None,
    stderr: str | None,
    return_code: int,
) -> str:
    """
    Build a meaningful message.

    Ruff, black and pytest report findings on STDOUT and leave STDERR empty,
    so relying on STDERR alone produces blank error messages.

    Either stream can be None when a decoding thread fails, so both are
    normalised defensively before use.
    """

    parts: list[str] = []

    if stdout and stdout.strip():
        parts.append(stdout.strip())

    if stderr and stderr.strip():
        parts.append(stderr.strip())

    if not parts:
        parts.append(f"Process exited with code {return_code} and no output.")

    return _truncate("\n".join(parts))


def _resolve_tool(module_name: str) -> list[str] | None:
    """
    Resolve a quality tool to an executable command.

    Prefers `python -m <tool>` so the tool matches the active interpreter.
    """

    probe = subprocess.run(
        [sys.executable, "-m", module_name, "--version"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )

    if probe.returncode == 0:
        return [sys.executable, "-m", module_name]

    binary = shutil.which(module_name)

    if binary:
        return [binary]

    return None


def _run_tool(
    check_name: str,
    module_name: str,
    arguments: list[str],
    project_path: str,
    success_codes: tuple[int, ...] = (0,),
) -> CheckResult:
    """
    Execute one quality tool and translate the outcome truthfully.
    """

    target = Path(project_path)

    if not target.exists():
        return CheckResult(
            check_name=check_name,
            passed=False,
            details=f"Target path does not exist: {target}",
            score=0.0,
        )

    try:
        command = _resolve_tool(module_name)
    except (subprocess.SubprocessError, OSError) as exc:
        return CheckResult(
            check_name=check_name,
            passed=False,
            details=f"Failed to probe '{module_name}': {exc}",
            score=0.0,
            skipped=True,
        )

    if command is None:
        return CheckResult(
            check_name=check_name,
            passed=False,
            details=(
                f"Tool '{module_name}' is not installed in this environment. "
                f"Check SKIPPED - install it to enforce this gate."
            ),
            score=0.0,
            skipped=True,
        )

    try:
        process = subprocess.run(
            command + arguments,
            cwd=str(target),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=_DEFAULT_TOOL_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return CheckResult(
            check_name=check_name,
            passed=False,
            details=(
                f"'{module_name}' exceeded the "
                f"{_DEFAULT_TOOL_TIMEOUT_SECONDS}s timeout."
            ),
            score=0.0,
        )
    except (subprocess.SubprocessError, OSError) as exc:
        return CheckResult(
            check_name=check_name,
            passed=False,
            details=f"Failed to execute '{module_name}': {exc}",
            score=0.0,
        )

    passed = process.returncode in success_codes

    details = _combine_output(
        process.stdout,
        process.stderr,
        process.returncode,
    )

    if passed and not details:
        details = f"{check_name} passed."

    return CheckResult(
        check_name=check_name,
        passed=passed,
        details=details,
        score=1.0 if passed else 0.0,
    )


class PytestValidator:
    """
    Validates unit and integration tests for the target project.
    """

    def validate(self, project_path: str) -> CheckResult:
        if os.environ.get(_PYTEST_ENV_MARKER):
            return CheckResult(
                check_name="pytest",
                passed=False,
                details=(
                    "Nested pytest execution refused to prevent runaway "
                    "process recursion. Check SKIPPED."
                ),
                score=0.0,
                skipped=True,
            )

        tests_directory = Path(project_path) / "tests"

        if not tests_directory.exists():
            return CheckResult(
                check_name="pytest",
                passed=False,
                details=f"No tests directory found at {tests_directory}. Check SKIPPED.",
                score=0.0,
                skipped=True,
            )

        # pytest exit code 5 means "no tests collected", which is not a failure
        # of the code under test.
        return _run_tool(
            check_name="pytest",
            module_name="pytest",
            arguments=["-q", str(tests_directory)],
            project_path=project_path,
            success_codes=(0, 5),
        )


class RuffValidator:
    """
    Validates code linting and style compliance.
    """

    def validate(self, project_path: str) -> CheckResult:
        return _run_tool(
            check_name="ruff",
            module_name="ruff",
            arguments=["check", "."],
            project_path=project_path,
        )


class BlackValidator:
    """
    Validates code formatting consistency.
    """

    def validate(self, project_path: str) -> CheckResult:
        return _run_tool(
            check_name="black",
            module_name="black",
            arguments=["--check", "."],
            project_path=project_path,
        )


class MypyValidator:
    """
    Validates static typing consistency.
    """

    def validate(self, project_path: str) -> CheckResult:
        target = Path(project_path)

        source_directory = target / "src"

        relative_target = "src" if source_directory.exists() else "."

        return _run_tool(
            check_name="mypy",
            module_name="mypy",
            arguments=[relative_target],
            project_path=project_path,
        )


class SecurityValidator:
    """
    Scans generated artifacts for dangerous constructs and plaintext secrets.

    Implemented as a deterministic AST + token scan so it has no external
    dependency and always produces a real verdict.
    """

    _DANGEROUS_CALLS = frozenset(
        {
            "eval",
            "exec",
            "compile",
        }
    )

    _SECRET_MARKERS = (
        "aws_secret_access_key",
        "api_key=",
        "apikey=",
        "password=",
        "secret_key=",
        "private_key=",
        "-----begin rsa private key-----",
        "-----begin openssh private key-----",
    )

    _SKIP_DIRECTORIES = frozenset(
        {
            ".git",
            ".venv",
            "venv",
            "__pycache__",
            "node_modules",
            "build",
            "dist",
            ".mypy_cache",
            ".pytest_cache",
            ".ruff_cache",
        }
    )

    def validate(self, project_path: str) -> CheckResult:
        target = Path(project_path)

        if not target.exists():
            return CheckResult(
                check_name="security",
                passed=False,
                details=f"Target path does not exist: {target}",
                score=0.0,
            )

        findings: list[str] = []
        scanned = 0

        for python_file in target.rglob("*.py"):
            if any(part in self._SKIP_DIRECTORIES for part in python_file.parts):
                continue

            try:
                source = python_file.read_text(
                    encoding="utf-8",
                    errors="replace",
                )
            except OSError as exc:
                findings.append(f"{python_file}: unreadable ({exc})")
                continue

            scanned += 1

            lowered = source.lower()

            for marker in self._SECRET_MARKERS:
                if marker in lowered:
                    findings.append(
                        f"{python_file}: possible hardcoded secret ('{marker}')"
                    )

            try:
                tree = ast.parse(source)
            except SyntaxError:
                # Syntax is the SyntaxValidator's responsibility, not ours.
                continue

            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue

                function = node.func

                name = (
                    function.id
                    if isinstance(function, ast.Name)
                    else getattr(function, "attr", None)
                )

                if name in self._DANGEROUS_CALLS:
                    findings.append(
                        f"{python_file}:{node.lineno}: dangerous call '{name}()'"
                    )

                if (
                    isinstance(function, ast.Attribute)
                    and function.attr in {"run", "call", "Popen", "check_output"}
                    and any(
                        keyword.arg == "shell"
                        and isinstance(keyword.value, ast.Constant)
                        and keyword.value.value is True
                        for keyword in node.keywords
                    )
                ):
                    findings.append(
                        f"{python_file}:{node.lineno}: subprocess call with shell=True"
                    )

        if scanned == 0:
            return CheckResult(
                check_name="security",
                passed=False,
                details=f"No Python sources found under {target}. Check SKIPPED.",
                score=0.0,
                skipped=True,
            )

        if findings:
            return CheckResult(
                check_name="security",
                passed=False,
                details=_truncate(
                    f"{len(findings)} security finding(s) across {scanned} file(s):\n"
                    + "\n".join(findings)
                ),
                score=0.0,
            )

        return CheckResult(
            check_name="security",
            passed=True,
            details=f"No dangerous calls or plaintext secrets across {scanned} file(s).",
            score=1.0,
        )


class ArchitectureValidator:
    """
    Validates Clean Architecture dependency direction.

    Enforced rule (DEVELOPMENT_RULES Rule 1 and Rule 3):
        domain must not import application, infrastructure or presentation.
        application must not import infrastructure or presentation.
    """

    _FORBIDDEN_BY_LAYER: dict[str, frozenset[str]] = {
        "domain": frozenset({"application", "infrastructure", "presentation"}),
        "application": frozenset({"infrastructure", "presentation"}),
    }

    _SKIP_DIRECTORIES = frozenset(
        {
            ".git",
            ".venv",
            "venv",
            "__pycache__",
            "node_modules",
            "build",
            "dist",
        }
    )

    def validate(self, project_path: str) -> CheckResult:
        target = Path(project_path)

        if not target.exists():
            return CheckResult(
                check_name="architecture",
                passed=False,
                details=f"Target path does not exist: {target}",
                score=0.0,
            )

        violations: list[str] = []
        inspected = 0

        for python_file in target.rglob("*.py"):
            if any(part in self._SKIP_DIRECTORIES for part in python_file.parts):
                continue

            layer = self._detect_layer(python_file)

            if layer is None:
                continue

            forbidden = self._FORBIDDEN_BY_LAYER[layer]

            try:
                tree = ast.parse(
                    python_file.read_text(
                        encoding="utf-8",
                        errors="replace",
                    )
                )
            except (OSError, SyntaxError):
                continue

            inspected += 1

            for node in ast.walk(tree):
                module_name = self._extract_module(node)

                if module_name is None:
                    continue

                segments = module_name.split(".")

                for banned in forbidden:
                    if banned in segments:
                        violations.append(
                            f"{python_file}:{getattr(node, 'lineno', 0)}: "
                            f"{layer} layer imports '{module_name}'"
                        )
                        break

        if inspected == 0:
            return CheckResult(
                check_name="architecture",
                passed=False,
                details=(
                    f"No domain/application layer packages found under {target}. "
                    f"Check SKIPPED."
                ),
                score=0.0,
                skipped=True,
            )

        if violations:
            return CheckResult(
                check_name="architecture",
                passed=False,
                details=_truncate(
                    f"{len(violations)} dependency-direction violation(s) "
                    f"across {inspected} file(s):\n" + "\n".join(violations)
                ),
                score=0.0,
            )

        return CheckResult(
            check_name="architecture",
            passed=True,
            details=(
                f"Clean Architecture dependency direction respected "
                f"across {inspected} file(s)."
            ),
            score=1.0,
        )

    def _detect_layer(self, python_file: Path) -> str | None:
        for part in python_file.parts:
            if part in self._FORBIDDEN_BY_LAYER:
                return part

        return None

    def _extract_module(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.ImportFrom):
            # Relative imports stay inside the current package, so they cannot
            # cross a layer boundary by name.
            if node.level and node.level > 0:
                return None

            return node.module

        if isinstance(node, ast.Import):
            return node.names[0].name if node.names else None

        return None


class SyntaxValidator:
    """
    Validates that every Python source file parses.

    This is the cheapest possible truth check on generated code and it has no
    external dependency, so it can never be skipped.
    """

    _SKIP_DIRECTORIES = frozenset(
        {
            ".git",
            ".venv",
            "venv",
            "__pycache__",
            "node_modules",
            "build",
            "dist",
        }
    )

    def validate(self, project_path: str) -> CheckResult:
        target = Path(project_path)

        if not target.exists():
            return CheckResult(
                check_name="syntax",
                passed=False,
                details=f"Target path does not exist: {target}",
                score=0.0,
            )

        errors: list[str] = []
        parsed = 0

        for python_file in target.rglob("*.py"):
            if any(part in self._SKIP_DIRECTORIES for part in python_file.parts):
                continue

            try:
                ast.parse(
                    python_file.read_text(
                        encoding="utf-8",
                        errors="replace",
                    )
                )
                parsed += 1
            except SyntaxError as exc:
                errors.append(f"{python_file}:{exc.lineno}: {exc.msg}")
            except OSError as exc:
                errors.append(f"{python_file}: unreadable ({exc})")

        if parsed == 0 and not errors:
            return CheckResult(
                check_name="syntax",
                passed=False,
                details=f"No Python sources found under {target}. Check SKIPPED.",
                score=0.0,
                skipped=True,
            )

        if errors:
            return CheckResult(
                check_name="syntax",
                passed=False,
                details=_truncate(
                    f"{len(errors)} syntax error(s) across {parsed + len(errors)} file(s):\n"
                    + "\n".join(errors)
                ),
                score=0.0,
            )

        return CheckResult(
            check_name="syntax",
            passed=True,
            details=f"All {parsed} Python file(s) parse successfully.",
            score=1.0,
        )


# Executed in a throwaway subprocess so that importing generated code can
# never mutate the gate's own interpreter state.
_IMPORT_PROBE = r'''
import importlib.util
import json
import pathlib
import sys
import traceback

root = pathlib.Path(sys.argv[1]).resolve()
source_root = root / "src" if (root / "src").is_dir() else root
sys.path.insert(0, str(source_root))

SKIP = {".git", ".venv", "venv", "__pycache__", "node_modules", "build", "dist"}

ok, failures = [], []

for path in sorted(source_root.rglob("*.py")):
    if any(part in SKIP for part in path.parts):
        continue
    if path.name == "__init__.py":
        continue

    rel = path.relative_to(source_root)
    module = ".".join(rel.with_suffix("").parts)

    try:
        spec = importlib.util.spec_from_file_location(module, path)
        if spec is None or spec.loader is None:
            failures.append((str(rel), "could not create module spec"))
            continue
        loaded = importlib.util.module_from_spec(spec)
        sys.modules[module] = loaded
        spec.loader.exec_module(loaded)
        ok.append(str(rel))
    except BaseException as exc:
        line = ""
        tb = traceback.extract_tb(sys.exc_info()[2])
        for frame in reversed(tb):
            if frame.filename == str(path):
                line = f":{frame.lineno}"
                break
        failures.append((str(rel) + line, f"{type(exc).__name__}: {exc}"))

print(json.dumps({"ok": ok, "failures": failures}))
'''


class ImportValidator:
    """
    Validates that generated modules can actually be imported.

    Rationale:
        A syntax check only proves a file parses. Generated code routinely
        parses while being completely unloadable, because the model emitted
        `from .models import Agent` for a module that was never written.
        ShadBotCore_BuiltByAgent passed the syntax check with 14 files of
        which 0 could be imported.

        This check is the difference between "the text is valid Python" and
        "the code exists".

    The probe runs in a subprocess: importing arbitrary generated code
    executes module-level statements, which must not touch the gate process.
    """

    def validate(self, project_path: str) -> CheckResult:
        target = Path(project_path)

        if not target.exists():
            return CheckResult(
                check_name="imports",
                passed=False,
                details=f"Target path does not exist: {target}",
                score=0.0,
                skipped=True,
            )

        source_root = target / "src" if (target / "src").is_dir() else target

        candidates = [
            path
            for path in source_root.rglob("*.py")
            if not any(
                part
                in {
                    ".git",
                    ".venv",
                    "venv",
                    "__pycache__",
                    "node_modules",
                    "build",
                    "dist",
                }
                for part in path.parts
            )
            and path.name != "__init__.py"
        ]

        if not candidates:
            return CheckResult(
                check_name="imports",
                passed=False,
                details=f"No importable Python modules under {source_root}. Check SKIPPED.",
                score=0.0,
                skipped=True,
            )

        try:
            completed = subprocess.run(
                [sys.executable, "-c", _IMPORT_PROBE, str(target)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=_DEFAULT_TOOL_TIMEOUT_SECONDS,
                cwd=str(target),
            )
        except subprocess.TimeoutExpired:
            return CheckResult(
                check_name="imports",
                passed=False,
                details=(
                    f"Import probe timed out after "
                    f"{_DEFAULT_TOOL_TIMEOUT_SECONDS}s. Generated code likely "
                    f"blocks at module level."
                ),
                score=0.0,
            )
        except OSError as exc:
            return CheckResult(
                check_name="imports",
                passed=False,
                details=f"Could not launch import probe: {exc}",
                score=0.0,
                skipped=True,
            )

        stdout = completed.stdout or ""

        payload: dict[str, object] | None = None

        for line in reversed(stdout.strip().splitlines()):
            if line.startswith("{"):
                try:
                    payload = json.loads(line)
                except ValueError:
                    payload = None
                break

        if payload is None:
            return CheckResult(
                check_name="imports",
                passed=False,
                details=_combine_output(
                    completed.stdout,
                    completed.stderr,
                    completed.returncode,
                ),
                score=0.0,
            )

        ok = list(payload.get("ok", []))
        failures = list(payload.get("failures", []))
        total = len(ok) + len(failures)

        if not failures:
            return CheckResult(
                check_name="imports",
                passed=True,
                details=f"All {total} generated module(s) import successfully.",
                score=1.0,
            )

        lines = [f"{name}: {reason}" for name, reason in failures]

        return CheckResult(
            check_name="imports",
            passed=False,
            details=_truncate(
                f"{len(failures)}/{total} module(s) cannot be imported:\n"
                + "\n".join(lines)
            ),
            score=round(len(ok) / total, 2) if total else 0.0,
        )


# Executed in a subprocess: this actually RUNS generated code.
_SMOKE_PROBE = r'''
import json
import pathlib
import runpy
import sys
import traceback

root = pathlib.Path(sys.argv[1]).resolve()
entry = pathlib.Path(sys.argv[2]).resolve()
source_root = root / "src" if (root / "src").is_dir() else root
sys.path.insert(0, str(source_root))
sys.argv = [str(entry)]

result = {"entry": str(entry.relative_to(root)), "ok": False, "error": ""}

# A __main__.py inside a package uses relative imports, which run_path cannot
# resolve. Execute it as `python -m package` instead so the parent package is
# known and the real runtime behaviour is exercised.
package = ""
if entry.name == "__main__.py":
    parts = entry.parent.relative_to(source_root).parts
    if parts:
        package = ".".join(parts)

try:
    if package:
        runpy.run_module(package, run_name="__main__", alter_sys=True)
    else:
        runpy.run_path(str(entry), run_name="__main__")
    result["ok"] = True
except SystemExit as exc:
    code = exc.code if exc.code is not None else 0
    result["ok"] = code == 0
    if not result["ok"]:
        result["error"] = f"exited with code {code}"
except BaseException as exc:
    tb = traceback.extract_tb(sys.exc_info()[2])
    where = ""
    for frame in reversed(tb):
        if frame.filename.endswith(".py") and str(root) in frame.filename:
            rel = pathlib.Path(frame.filename)
            try:
                rel = rel.relative_to(root)
            except ValueError:
                pass
            where = f" at {rel}:{frame.lineno}"
            break
    result["error"] = f"{type(exc).__name__}: {exc}{where}"

print("SHADBOT_SMOKE_RESULT " + json.dumps(result))
'''


class SmokeRunValidator:
    """
    Validates that the generated project actually RUNS.

    Rationale:
        ImportValidator proves modules load. It does not prove they work:
        importing a module executes only its top-level statements, so a broken
        call inside main() is invisible.

        Run 2 of ShadBotCore_BuiltByAgent passed both syntax and imports and
        the gate reported GREEN, yet `python -m agentplatform` died with
        `TypeError: 'dict' object is not callable` because a @property was
        called like a function.

        This check closes that hole: it executes each entry point and fails on
        a non-zero exit or any uncaught exception.

    Entry points probed, in priority order:
        run.py, main.py, __main__.py, src/<pkg>/__main__.py

    A project with no entry point is SKIPPED, never passed.
    """

    _ENTRY_CANDIDATES = ("run.py", "main.py", "__main__.py")

    def _find_entry_points(self, target: Path) -> list[Path]:
        found: list[Path] = []

        for name in self._ENTRY_CANDIDATES:
            candidate = target / name
            if candidate.is_file():
                found.append(candidate)

        source_root = target / "src" if (target / "src").is_dir() else target

        for candidate in sorted(source_root.rglob("__main__.py")):
            if any(
                part in {".git", ".venv", "venv", "__pycache__", "node_modules"}
                for part in candidate.parts
            ):
                continue
            if candidate not in found:
                found.append(candidate)

        return found

    def validate(self, project_path: str) -> CheckResult:
        target = Path(project_path)

        if not target.exists():
            return CheckResult(
                check_name="smoke_run",
                passed=False,
                details=f"Target path does not exist: {target}",
                score=0.0,
                skipped=True,
            )

        entries = self._find_entry_points(target)

        if not entries:
            return CheckResult(
                check_name="smoke_run",
                passed=False,
                details=(
                    "No entry point (run.py / main.py / __main__.py) found. "
                    "Check SKIPPED - generated projects should expose one."
                ),
                score=0.0,
                skipped=True,
            )

        failures: list[str] = []
        succeeded: list[str] = []

        for entry in entries:
            try:
                completed = subprocess.run(
                    [sys.executable, "-c", _SMOKE_PROBE, str(target), str(entry)],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=_DEFAULT_TOOL_TIMEOUT_SECONDS,
                    cwd=str(target),
                )
            except subprocess.TimeoutExpired:
                failures.append(
                    f"{entry.name}: timed out after "
                    f"{_DEFAULT_TOOL_TIMEOUT_SECONDS}s (blocking call or "
                    f"infinite loop)"
                )
                continue
            except OSError as exc:
                return CheckResult(
                    check_name="smoke_run",
                    passed=False,
                    details=f"Could not launch smoke probe: {exc}",
                    score=0.0,
                    skipped=True,
                )

            payload: dict[str, object] | None = None

            for line in (completed.stdout or "").splitlines():
                if line.startswith("SHADBOT_SMOKE_RESULT "):
                    try:
                        payload = json.loads(
                            line[len("SHADBOT_SMOKE_RESULT ") :]
                        )
                    except ValueError:
                        payload = None
                    break

            if payload is None:
                failures.append(
                    f"{entry.name}: probe produced no result. "
                    + _combine_output(
                        completed.stdout,
                        completed.stderr,
                        completed.returncode,
                    )
                )
                continue

            if payload.get("ok"):
                succeeded.append(str(payload.get("entry", entry.name)))
            else:
                failures.append(
                    f"{payload.get('entry', entry.name)}: {payload.get('error')}"
                )

        total = len(succeeded) + len(failures)

        if not failures:
            return CheckResult(
                check_name="smoke_run",
                passed=True,
                details=(
                    f"All {total} entry point(s) ran successfully: "
                    + ", ".join(succeeded)
                ),
                score=1.0,
            )

        return CheckResult(
            check_name="smoke_run",
            passed=False,
            details=_truncate(
                f"{len(failures)}/{total} entry point(s) failed to run:\n"
                + "\n".join(failures)
            ),
            score=round(len(succeeded) / total, 2) if total else 0.0,
        )
