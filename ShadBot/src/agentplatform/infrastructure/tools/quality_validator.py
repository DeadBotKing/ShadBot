"""
ShadBot Agent Platform

Quality validation tool.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


class QualityValidator:
    """
    Executes enterprise quality validation pipeline.
    """

    def validate(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Run complete project quality validation.

        Individual check failures are reported in the result. This method
        must not raise, otherwise QA/Reviewer abort the whole pipeline
        with an empty RuntimeError when a linter writes only to stdout.
        """
        project = Path(path)
        cwd = project if project.exists() else Path(".")

        # Running pytest from inside a pytest process forks without bound.
        nested = bool(os.environ.get("PYTEST_CURRENT_TEST"))

        checks: dict[str, dict[str, object]] = {
            "ruff": self._run([sys.executable, "-m", "ruff", "check", "."], cwd),
            "black": self._run([sys.executable, "-m", "black", "--check", "."], cwd),
            "mypy": self._run([sys.executable, "-m", "mypy", "src"], cwd),
        }

        if nested:
            checks["pytest"] = {
                "success": False,
                "skipped": True,
                "return_code": None,
                "output": (
                    "Nested pytest execution refused to prevent runaway "
                    "process recursion."
                ),
                "command": "pytest",
            }
        else:
            checks["pytest"] = self._run(
                [sys.executable, "-m", "pytest", "-q"],
                cwd,
                success_codes=(0, 5),
            )

        executed = {
            name: item
            for name, item in checks.items()
            if not item.get("skipped")
        }

        # An all-skipped run proves nothing and must not be reported as PASS.
        passed = bool(executed) and all(
            bool(item.get("success")) for item in executed.values()
        )

        return {
            "status": "PASS" if passed else "FAIL",
            "success": passed,
            "checks": checks,
            "executed": len(executed),
            "total": len(checks),
            "path": str(cwd),
        }

    def _run(
        self,
        command: list[str],
        path: Path,
        success_codes: tuple[int, ...] = (0,),
    ) -> dict[str, object]:
        try:
            # shell=False: arguments are passed as a list, so no shell
            # injection is possible and no shell process is spawned.
            result = subprocess.run(
                command,
                cwd=str(path),
                shell=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=180,
            )
            output = "\n".join(
                part
                for part in (result.stdout or "", result.stderr or "")
                if part.strip()
            ).strip()
            if not output:
                output = f"Process exited with code {result.returncode}."

            return {
                "success": result.returncode in success_codes,
                "return_code": result.returncode,
                "output": output,
                "command": " ".join(command),
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "return_code": -1,
                "output": f"Command timed out after 180s: {' '.join(command)}",
                "command": " ".join(command),
            }
        except (subprocess.SubprocessError, OSError) as exc:
            detail = str(exc).strip() or type(exc).__name__
            return {
                "success": False,
                "return_code": -1,
                "output": detail,
                "command": " ".join(command),
            }
