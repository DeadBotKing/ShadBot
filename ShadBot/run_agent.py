"""
ShadBot Agent Platform Runner
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from uuid import uuid4

_src_dir = (Path(__file__).resolve().parent / "src").resolve()
if _src_dir.exists() and str(_src_dir) not in sys.path:
    sys.path.insert(0, str(_src_dir))

from agentplatform.application.bootstrap import (
    AgentPlatformBootstrap,
)
from agentplatform.application.loop.project_execution import (
    ProjectExecutionService,
)
from agentplatform.application.workspace.workspace_factory import (
    WorkspaceFactory,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.workspace import (
    Project,
)


SHADBOT_BUILD = "2026-08-13-qafix"


def _print_build_banner() -> None:
    print("=" * 75)
    print(f"SHADBOT BUILD: {SHADBOT_BUILD}")
    try:
        from agentplatform.infrastructure.tools import (
            experiment_executor_adapter as _ee,
        )

        print(f"EXPERIMENT ADAPTER FILE: {_ee.__file__}")
        source = getattr(_ee, "SHADBOT_BUILD", "UNKNOWN")
        print(f"EXPERIMENT ADAPTER BUILD: {source}")
        if "Experiment command required" in open(
            _ee.__file__,
            encoding="utf-8",
            errors="replace",
        ).read():
            print(
                "WARNING: Loaded experiment_executor_adapter.py still contains "
                "the old 'Experiment command required' raise. You are NOT "
                "running the MLFIX2 files."
            )
    except Exception as exc:
        print(f"EXPERIMENT ADAPTER DIAGNOSTIC FAILED: {exc}")
    print("=" * 75)


def main() -> int:
    _print_build_banner()

    parser = argparse.ArgumentParser(
        description="ShadBot Agent Platform",
    )

    parser.add_argument(
        "--project",
        default="ShadBotCore_BuiltByAgent",
        help="Workspace project (e.g. ShadBotCore_BuiltByAgent, Meryx).",
    )

    args = parser.parse_args()

    _local_ws = (Path(__file__).parent / "ShadBotWorkspace").resolve()
    if _local_ws.exists():
        workspace_root = _local_ws
    else:
        workspace_root = (Path(__file__).parent / ".." / "ShadBotWorkspace").resolve()

    project_path = workspace_root / args.project

    bootstrap = AgentPlatformBootstrap()

    execution_loop = bootstrap.build()

    project_executor = ProjectExecutionService(
        execution_loop=execution_loop,
    )

    project = Project(
        name=args.project,
        path=project_path,
        project_type="software",
    )

    workspace = WorkspaceFactory().create(
        name="ShadBotWorkspace",
        root_path=workspace_root,
        projects=(project,),
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Execute selected project task.",
        workspace=workspace,
        target_project=project,
    )

    results = project_executor.execute_project(
        project_path=project_path,
        context=context,
    )

    total_time = sum(float(r.data.get("elapsed_seconds", 0.0)) for r in results)

    print()
    print("=" * 75)
    print(f"Project Execution Summary : {args.project}")
    print(f"Total Pipeline Elapsed Time : {total_time:.2f} seconds")
    print("=" * 75)

    for index, result in enumerate(
        results,
        start=1,
    ):
        elapsed = float(result.data.get("elapsed_seconds", 0.0))
        agent_name = str(result.data.get("agent", f"agent_{index}")).ljust(22)
        status_str = "SUCCESS" if result.success else "FAILED"

        print(
            f"[{index}] {agent_name} {status_str:<8} "
            f"{elapsed:>7.2f}s  {result.message}"
        )

    failed = [result for result in results if not result.success]

    print("=" * 75)
    print(
        f"Agents: {len(results)} | "
        f"Succeeded: {len(results) - len(failed)} | "
        f"Failed: {len(failed)}"
    )
    print("=" * 75)

    # Exit non-zero on failure so CI and shell callers can detect it.
    return 1 if failed or not results else 0


if __name__ == "__main__":
    sys.exit(main())
