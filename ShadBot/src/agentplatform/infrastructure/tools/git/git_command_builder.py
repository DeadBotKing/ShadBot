"""
ShadBot Agent Platform

Git Command Builder
"""

from __future__ import annotations

from .git_operation import GitOperation


class GitCommandBuilder:
    """
    Builds git commands.
    """

    def build(
        self,
        operation: GitOperation,
        arguments: tuple[str, ...] = (),
    ) -> list[str]:

        commands = {
            GitOperation.STATUS: [
                "git",
                "status",
            ],
            GitOperation.DIFF: [
                "git",
                "diff",
            ],
            GitOperation.LOG: [
                "git",
                "log",
            ],
            GitOperation.BRANCH: [
                "git",
                "branch",
            ],
            GitOperation.ADD: [
                "git",
                "add",
            ],
            GitOperation.COMMIT: [
                "git",
                "commit",
            ],
            GitOperation.CHECKOUT: [
                "git",
                "checkout",
            ],
        }

        command = commands.get(
            operation,
        )

        if command is None:
            raise ValueError(
                "Unsupported git operation",
            )

        command.extend(
            arguments,
        )

        return command
