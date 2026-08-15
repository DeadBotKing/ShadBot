"""
ShadBot Agent Platform

Agent Process Controller component for 7.1 Agent Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from .agent_runtime_instance import AgentRuntimeInstance


class AgentProcessController:
    """
    Controls safe execution of an agent within its runtime instance.
    """

    def execute_instance(self, instance: AgentRuntimeInstance, context: AgentExecutionContext) -> AgentResult:
        try:
            return instance.agent.execute(context)
        except Exception as exc:
            return AgentResult(
                success=False,
                message=str(exc),
                data={"agent": instance.agent.name, "error": type(exc).__name__},
            )
