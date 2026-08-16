#!/usr/bin/env python3
"""
ShadBot Autonomously Generated Runner for ShadBotCore_BuiltByAgent.

Imports every generated module so that a broken build fails here
with a non-zero exit code instead of silently reporting success.
"""

from __future__ import annotations

import importlib
import pkgutil
import sys
import traceback
from pathlib import Path


def main() -> int:
    """Import all generated modules; return 0 only if all succeed."""

    print("Starting ShadBotCore_BuiltByAgent...")

    src_dir = Path(__file__).parent / "src"
    root = src_dir if src_dir.is_dir() else Path(__file__).parent
    sys.path.insert(0, str(root))

    failures: list[str] = []
    checked = 0

    for module_info in pkgutil.walk_packages(
        [str(root)],
        prefix="",
    ):
        if "__main__" in module_info.name:
            continue
        try:
            importlib.import_module(module_info.name)
            checked += 1
        except Exception:
            failures.append(
                f"{module_info.name}:\n"
                + traceback.format_exc(limit=3)
            )

    if failures:
        print(f"FAILED: {len(failures)} module(s) could not be imported.")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(f"OK: {checked} module(s) imported successfully.")
    print("Project ShadBotCore_BuiltByAgent is operational.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
