"""
ShadBot Agent Platform

Agent runner.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.bootstrap import (
    AgentPlatformBootstrap,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.tasks import (
    AgentTask,
    TaskType,
)


class AgentRunner:
    """
    Executes agents against selected project.
    """

    def __init__(self) -> None:
        self._loop = AgentPlatformBootstrap().build()

    def run(
        self,
        project_name: str,
        instructions: str,
    ) -> None:

        print(
            f"[AgentRunner] Target project: {project_name}",
        )

        print(
            f"[AgentRunner] Instruction: {instructions}",
        )

        context = AgentExecutionContext(
            project_id=uuid4(),
            task_id=uuid4(),
            instructions=instructions,
            metadata={
                "workspace": "ShadBotWorkspace",
                "project": project_name,
            },
        )

        task = AgentTask(
            title=instructions,
            description=instructions,
            task_type=TaskType.IMPLEMENTATION,
        )

        results = self._loop.execute(
            task,
            context,
        )

        for result in results:
            print(
                f"[Agent Result] {result.message}",
            )

        print(
            "[AgentRunner] Completed.",
        )
