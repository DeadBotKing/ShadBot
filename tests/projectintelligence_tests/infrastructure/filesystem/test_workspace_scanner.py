"""
Tests for WorkspaceScanner
"""

from pathlib import Path

from projectintelligence.infrastructure.filesystem.directory_walker import (
    DirectoryWalker,
)
from projectintelligence.infrastructure.filesystem.file_collector import (
    FileCollector,
)
from projectintelligence.infrastructure.filesystem.ignore_manager import (
    IgnoreManager,
)
from projectintelligence.infrastructure.filesystem.workspace_scanner import (
    WorkspaceScanner,
)


def test_should_scan_workspace_and_return_allowed_files(
    tmp_path: Path,
) -> None:
    workspace = tmp_path / "workspace"

    source_directory = workspace / "src"
    ignored_directory = workspace / ".git"

    source_directory.mkdir(parents=True)
    ignored_directory.mkdir(parents=True)

    python_file = source_directory / "app.py"
    git_file = ignored_directory / "config"

    python_file.write_text("print('hello')")
    git_file.write_text("ignored")

    scanner = WorkspaceScanner(
        directory_walker=DirectoryWalker(),
        ignore_manager=IgnoreManager(),
        file_collector=FileCollector(),
    )

    files = scanner.scan(workspace)

    assert python_file in files
    assert git_file not in files
