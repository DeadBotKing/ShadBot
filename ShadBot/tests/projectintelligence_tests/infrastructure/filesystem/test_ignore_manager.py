from pathlib import Path

from projectintelligence.infrastructure.filesystem.ignore_manager import IgnoreManager


def test_should_ignore_git_directory() -> None:
    manager = IgnoreManager()

    assert manager.should_ignore(
        Path(".git/config"),
    )


def test_should_not_ignore_python_file() -> None:
    manager = IgnoreManager()

    assert not manager.should_ignore(
        Path("src/main.py"),
    )
