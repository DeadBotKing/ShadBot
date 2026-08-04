"""
ShadBot Agent Platform Runner
"""

from __future__ import annotations

import argparse
from pathlib import Path
from uuid import uuid4

from agentplatform.application.bootstrap import (
    AgentPlatformBootstrap,
)
from agentplatform.application.loop.project_execution import (
    ProjectExecutionService,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ShadBot Agent Platform",
    )

    parser.add_argument(
        "--project",
        required=True,
        choices=[
            "Meryx",
            "Trader",
        ],
        help="Workspace project.",
    )

    args = parser.parse_args()

    workspace_root = (
        Path(__file__).parent
        / ".."
        / "ShadBotWorkspace"
    ).resolve()

    project_path = workspace_root / args.project

    bootstrap = AgentPlatformBootstrap()

    execution_loop = bootstrap.build()

    project_executor = ProjectExecutionService(
        execution_loop=execution_loop,
    )

    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Execute selected project task.",
    )

    results = project_executor.execute_project(
        project_path=project_path,
        context=context,
    )

    print()
    print("=" * 70)
    print(f"Project : {args.project}")
    print(f"Executed Results : {len(results)}")
    print("=" * 70)

    for index, result in enumerate(
        results,
        start=1,
    ):
        print(
            f"[{index}] success={result.success} "
            f"message={result.message}"
        )


if __name__ == "__main__":
    main()