"""
ShadBot Project Intelligence

CLI Entry Point
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Project Intelligence Engine",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
    )

    analyze_parser.add_argument(
        "workspace",
        type=Path,
    )

    analyze_parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "project_intelligence.json",
        ),
    )

    args = parser.parse_args()

    if args.command == "analyze":
        print(
            "Project Intelligence runtime initialized",
        )
        print(
            f"Workspace: {args.workspace}",
        )
        print(
            f"Output: {args.output}",
        )


if __name__ == "__main__":
    main()
