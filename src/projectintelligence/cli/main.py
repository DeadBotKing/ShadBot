"""
ShadBot Project Intelligence

CLI Entry Point
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from projectintelligence.application.bootstrap.project_intelligence_bootstrap import (
    ProjectIntelligenceBootstrap,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="shadbot-intelligence",
        description="Analyze a software project and generate an Intelligence Package.",
    )

    parser.add_argument(
        "workspace",
        type=Path,
        help="Path to the project workspace.",
    )

    parser.add_argument(
        "--name",
        type=str,
        default=None,
        help="Override project name.",
    )

    return parser


def main() -> int:
    parser = build_parser()

    args = parser.parse_args()

    workspace = args.workspace.resolve()

    if not workspace.exists():
        print(
            f"Workspace does not exist: {workspace}",
            file=sys.stderr,
        )
        return 1

    if not workspace.is_dir():
        print(
            f"Workspace is not a directory: {workspace}",
            file=sys.stderr,
        )
        return 1

    project = ProjectEntity(
        name=args.name or workspace.name,
        workspace=workspace,
        repository_path=workspace,
    )

    bootstrap = ProjectIntelligenceBootstrap()

    engine = bootstrap.build(
        project=project,
    )

    engine.execute(
        project=project,
    )

    print("Project Intelligence completed successfully.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
