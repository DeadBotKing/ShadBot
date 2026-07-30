"""
Tests for FileCollector
"""

from pathlib import Path

from projectintelligence.infrastructure.filesystem.file_collector import (
    FileCollector,
)


def test_should_collect_only_files(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"

    workspace.mkdir()

    file_one = workspace / "main.py"
    file_two = workspace / "config.json"
    directory = workspace / "src"

    file_one.write_text("print('hello')")
    file_two.write_text("{}")
    directory.mkdir()

    collector = FileCollector()

    collected = collector.collect(
        [
            file_one,
            file_two,
            directory,
        ]
    )

    assert file_one in collected
    assert file_two in collected
    assert directory not in collected
