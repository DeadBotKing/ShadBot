"""
Tests for DirectoryWalker
"""

from pathlib import Path

from projectintelligence.infrastructure.filesystem.directory_walker import (
    DirectoryWalker,
)


def test_should_walk_all_paths_in_workspace(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"

    source_directory = workspace / "src"
    source_directory.mkdir(parents=True)

    python_file = source_directory / "app.py"
    config_file = workspace / "config.json"

    python_file.write_text("print('hello')")
    config_file.write_text("{}")

    walker = DirectoryWalker()

    paths = list(walker.walk(workspace))

    assert source_directory in paths
    assert python_file in paths
    assert config_file in paths
