"""
ShadBot Agent Platform

Unified service for 7.1 Agent Runtime.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult
from .agent_runtime_instance import AgentRuntimeInstance
from .lifecycle_manager import AgentLifecycleManager
from .process_controller import AgentProcessController
from .runtime_monitor import AgentRuntimeHealth, AgentRuntimeMonitor


class AgentRuntimeServiceLayer:
    """
    Orchestrates agent runtime lifecycle, process execution, and monitoring.
    """

    def __init__(
        self,
        lifecycle: AgentLifecycleManager | None = None,
        controller: AgentProcessController | None = None,
        monitor: AgentRuntimeMonitor | None = None,
    ) -> None:
        self._lifecycle = lifecycle or AgentLifecycleManager()
        self._controller = controller or AgentProcessController()
        self._monitor = monitor or AgentRuntimeMonitor()

    def run_agent(self, agent: AgentContract, context: AgentExecutionContext) -> tuple[AgentResult, AgentRuntimeHealth]:
        instance = self._lifecycle.create_instance(agent)
        running = self._lifecycle.start_instance(instance)
        res = self._controller.execute_instance(running, context)
        terminated = self._lifecycle.terminate_instance(running, res.success)
        health = self._monitor.inspect(terminated)
        return res, health
