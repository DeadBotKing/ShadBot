"""
ShadBot Agent Platform

Agent orchestrator implementation with real-time execution monitoring,
Phase 6 Orchestration sub-services (6.1-6.7), Phase 8 Communication
services (8.1-8.3), Phase 9 Quality Gate, Phase 10 Self Improvement,
Phase 11 Platform Finalization, and Phase 12 Production Freeze V1.0.
"""

from __future__ import annotations

import time
from dataclasses import replace
from typing import Sequence
from uuid import uuid4

from agentplatform.application.communication.agent_messaging import (
    AgentMessagingService,
)
from agentplatform.application.communication.event_bus import (
    EventBusService,
)
from agentplatform.application.communication.workflow_events import (
    WorkflowEventsService,
)
from agentplatform.application.execution import (
    AgentExecutionService as ExecutionService,
)
from agentplatform.application.orchestration.agent_handoff import (
    AgentHandoffService,
    HandoffRequest,
)
from agentplatform.application.orchestration.failure_recovery import (
    FailureRecoveryService,
)
from agentplatform.application.orchestration.orchestration_monitoring import (
    OrchestrationMonitoringService,
)
from agentplatform.application.orchestration.pipeline_management import (
    PipelineManagementService,
)
from agentplatform.application.orchestration.result_aggregation import (
    ResultAggregationService,
)
from agentplatform.application.platform import (
    PlatformFinalizationService,
)
from agentplatform.application.quality_gate import (
    DeterministicQualityGate,
    QualityGateServiceLayer,
)
from agentplatform.application.release import (
    ProductionReleaseService,
)
from agentplatform.application.self_improvement import (
    SelfImprovementServiceLayer,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.contracts import (
    AgentContract,
)
from agentplatform.domain.results import (
    AgentResult,
)


class AgentOrchestrator:
    """
    Coordinates execution of multiple agents with real-time progress reporting,
    pipeline tracking, context handoffs, failure recovery, result aggregation,
    orchestration monitoring (Phase 6), communication events (Phase 8),
    quality gates (Phase 9), self improvement (Phase 10), platform finalization
    (Phase 11), and production freeze V1.0 (Phase 12).
    """

    def __init__(
        self,
        execution_service: ExecutionService | None = None,
        pipeline_mgr: PipelineManagementService | None = None,
        handoff_srv: AgentHandoffService | None = None,
        aggregation_srv: ResultAggregationService | None = None,
        recovery_srv: FailureRecoveryService | None = None,
        monitoring_srv: OrchestrationMonitoringService | None = None,
        event_bus: EventBusService | None = None,
        messaging_srv: AgentMessagingService | None = None,
        workflow_events: WorkflowEventsService | None = None,
        quality_gate_srv: QualityGateServiceLayer | None = None,
        deterministic_gate: DeterministicQualityGate | None = None,
        self_improvement_srv: SelfImprovementServiceLayer | None = None,
        platform_srv: PlatformFinalizationService | None = None,
        release_srv: ProductionReleaseService | None = None,
        max_iterations: int = 3,
    ) -> None:
        self._execution_service = execution_service or ExecutionService()
        self.pipeline_mgr = pipeline_mgr or PipelineManagementService()
        self.handoff_srv = handoff_srv or AgentHandoffService()
        self.aggregation_srv = aggregation_srv or ResultAggregationService()
        self.recovery_srv = recovery_srv or FailureRecoveryService()
        self.monitoring_srv = monitoring_srv or OrchestrationMonitoringService()
        self.event_bus = event_bus or EventBusService()
        self.messaging_srv = messaging_srv or AgentMessagingService()
        self.workflow_events = workflow_events or WorkflowEventsService()
        self.quality_gate_srv = quality_gate_srv or QualityGateServiceLayer()
        self.deterministic_gate = deterministic_gate or DeterministicQualityGate()
        self.self_improvement_srv = self_improvement_srv or SelfImprovementServiceLayer()
        self.platform_srv = platform_srv or PlatformFinalizationService()
        self.release_srv = release_srv or ProductionReleaseService()
        self._max_iterations = max_iterations

    def execute_pipeline(
        self,
        agents: Sequence[AgentContract],
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute ordered agent pipeline with Phase 6 services, Phase 8 Communication
        events/messaging, and real-time elapsed time monitoring.
        """
        results: list[AgentResult] = []
        current_context = context
        start_time = time.time()

        task_title = context.task_title or "Orchestrated Pipeline Task"
        pipeline, pipe_state = self.pipeline_mgr.create_pipeline(task_title, agents)

        # 1. Emit Workflow Event & Publish EventBus for Pipeline Start (8.1 & 8.3)
        self.workflow_events.emit(
            workflow_id=pipeline.pipeline_id,
            state="STARTED",
            step=0,
            payload={"agents_count": len(agents), "task_title": task_title},
        )
        self.event_bus.publish(
            event_type="PIPELINE_STARTED",
            source="AgentOrchestrator",
            payload={"pipeline_id": str(pipeline.pipeline_id), "task_id": str(context.task_id)},
        )

        print("\n" + "=" * 75)
        print(f"[ORCHESTRATOR START] Executing Pipeline (ID: {pipeline.pipeline_id}) with {len(agents)} Agents")
        print("=" * 75)

        for _ in range(self._max_iterations):
            iteration_results: list[AgentResult] = []

            for idx, agent in enumerate(agents, start=1):
                step = pipeline.steps[idx - 1] if idx <= len(pipeline.steps) else None
                if step and not self.pipeline_mgr.check_ready(step, pipe_state):
                    raise RuntimeError(f"Pipeline step {idx} ({agent.name}) is not ready for execution.")

                # Publish Agent Start Events (8.1 & 8.3)
                self.workflow_events.emit(
                    workflow_id=pipeline.pipeline_id,
                    state="RUNNING",
                    step=idx,
                    payload={"agent": agent.name},
                )
                self.event_bus.publish(
                    event_type="AGENT_STARTED",
                    source=agent.name,
                    payload={"step": idx},
                )

                print("\n" + "-" * 75)
                print(f"[AGENT START] Role: {agent.name.upper()} (Step {idx}/{len(agents)})")
                print("-" * 75)

                step_started = time.time()
                result = self._execution_service.execute(
                    agent,
                    current_context,
                )

                elapsed_raw = result.data.get("elapsed_seconds", 0.0)
                try:
                    elapsed = float(elapsed_raw or 0.0)
                except (TypeError, ValueError):
                    elapsed = 0.0
                if elapsed <= 0.0:
                    elapsed = time.time() - step_started
                status_str = "SUCCESS" if result.success else "FAILED"

                self.monitoring_srv.log_execution(
                    context.execution_id,
                    agent.name,
                    elapsed * 1000.0,
                    result.success,
                )

                print("-" * 75)
                print(f"[AGENT COMPLETED: {agent.name.upper()}] Status: {status_str} | Elapsed: {elapsed:.2f}s")
                if not result.success:
                    print(f"[AGENT ERROR] {result.message}")
                print("-" * 75)

                iteration_results.append(
                    result,
                )

                if result.success:
                    # Publish Agent Complete Events & Send Direct Agent Message (8.1, 8.2, 8.3)
                    self.event_bus.publish(
                        event_type="AGENT_COMPLETED",
                        source=agent.name,
                        payload={"step": idx, "elapsed_seconds": elapsed},
                    )
                    self.workflow_events.emit(
                        workflow_id=pipeline.pipeline_id,
                        state="RUNNING",
                        step=idx,
                        payload={"status": "SUCCESS", "agent": agent.name},
                    )
                    next_name = agents[idx].name if idx < len(agents) else "orchestrator"
                    self.messaging_srv.send_message(
                        sender=agent.name,
                        receiver=next_name,
                        msg_type="STAGE_HANDOFF_MESSAGE",
                        payload={"step_completed": idx, "message": result.message},
                        priority="CRITICAL",
                    )

                    req = HandoffRequest(
                        source_agent_name=agent.name,
                        target_agent_name=next_name,
                        previous_result=result,
                        task_id=context.task_id,
                    )
                    handoff_pkg = self.handoff_srv.handoff(current_context, req)
                    current_context = handoff_pkg.context

                    if step:
                        pipe_state, _ = self.pipeline_mgr.advance_pipeline(pipeline, step.step_number)
                else:
                    # Publish Agent Failed Events & Send Critical Alert Message (8.1, 8.2, 8.3)
                    self.event_bus.publish(
                        event_type="AGENT_FAILED",
                        source=agent.name,
                        payload={"step": idx, "error": result.message},
                    )
                    self.workflow_events.emit(
                        workflow_id=pipeline.pipeline_id,
                        state="FAILED",
                        step=idx,
                        payload={"error": result.message},
                    )
                    self.messaging_srv.send_message(
                        sender=agent.name,
                        receiver="orchestrator",
                        msg_type="STAGE_FAILED_MESSAGE",
                        payload={"step_failed": idx, "error": result.message},
                        priority="CRITICAL",
                    )

                    recovery_pkg = self.recovery_srv.recover([result], current_attempt=1)
                    strategy_name = recovery_pkg.strategies[0].strategy_name if recovery_pkg.strategies else "ABORT"
                    print(f"[FATAL ORCHESTRATION ALERT] Agent '{agent.name}' failed: {result.message}")
                    print(f"[RECOVERY STRATEGY SELECTED] {strategy_name}")
                    print("[FATAL ORCHESTRATION ALERT] Halting pipeline to prevent silent skip or fake execution.")
                    return iteration_results

                if (
                    agent.name == "architect"
                    and "architecture_plan" not in current_context.metadata
                ):
                    raise RuntimeError(
                        f"Architect result missing architecture_plan propagation. Error: {result.message}",
                    )

            if not self._needs_retry(
                iteration_results,
            ):
                results.extend(
                    iteration_results,
                )
                break

        total_elapsed_ms = (time.time() - start_time) * 1000.0
        agg_pkg, _ = self.aggregation_srv.aggregate(results)
        metrics = self.monitoring_srv.generate_metrics(
            pipeline.pipeline_id,
            total_elapsed_ms,
            len(agents),
            agg_pkg.success,
        )

        from pathlib import Path
        project_path_str = str(current_context.metadata.get("project_path", "."))
        project_path = Path(project_path_str)
        if not project_path.exists():
            project_path = Path(".")

        det_report = self.deterministic_gate.verify_deterministic(project_path)
        qg_report, qg_decision = self.quality_gate_srv.validate_project(current_context.project_id, str(project_path))

        det_dict = det_report.to_dict() if hasattr(det_report, "to_dict") else det_report.__dict__
        qg_dict = qg_report.to_dict() if hasattr(qg_report, "to_dict") else qg_report.__dict__
        dec_dict = qg_decision.to_dict() if hasattr(qg_decision, "to_dict") else qg_decision.__dict__

        current_context.metadata["deterministic_gate_report"] = det_dict
        current_context.metadata["quality_gate_report"] = qg_dict
        current_context.metadata["repair_loop_decision"] = dec_dict
        context.metadata["deterministic_gate_report"] = det_dict
        context.metadata["quality_gate_report"] = qg_dict
        context.metadata["repair_loop_decision"] = dec_dict

        print("\n" + "=" * 75)
        print(f"[QUALITY GATE ENFORCEMENT] Deterministic Gate: {'GREEN' if det_report.passed else 'FAIL'} | Quality Gate Approved: {qg_report.approved} | Overall Score: {qg_report.overall_score}")
        if qg_decision.trigger_repair:
            print(f"[REPAIR LOOP TRIGGERED] Target Agent: '{qg_decision.target_agent}' | Instructions: {qg_decision.repair_instructions}")
        print("=" * 75)

        self.event_bus.publish(
            event_type="QUALITY_GATE_EVALUATED",
            source="AgentOrchestrator",
            payload={
                "pipeline_id": str(pipeline.pipeline_id),
                "approved": qg_report.approved,
                "deterministic_passed": det_report.passed,
                "score": qg_report.overall_score,
            },
        )
        if qg_decision.trigger_repair:
            self.event_bus.publish(
                event_type="REPAIR_LOOP_TRIGGERED",
                source="QualityGateServiceLayer",
                payload={
                    "target_agent": qg_decision.target_agent,
                    "instructions": qg_decision.repair_instructions,
                },
            )

        si_summary = self.self_improvement_srv.get_cycle_summary(results)
        current_context.metadata["self_improvement_report"] = si_summary
        context.metadata["self_improvement_report"] = si_summary

        ana_dict = si_summary["reflection_analysis"]
        evo_dict = si_summary["brain_evolution"]

        print("\n" + "=" * 75)
        print(f"[SELF IMPROVEMENT CYCLE] Success Ratio: {ana_dict['success_ratio']:.2f} | Trend: {si_summary['performance_trend']['status']} | Potential: {ana_dict['learning_potential']}")
        print(f"[BRAIN EVOLUTION] Evolved: {evo_dict['evolved']} | Version: {evo_dict['version']} | Summary: {evo_dict['evolution_summary']}")
        print("=" * 75)

        self.event_bus.publish(
            event_type="SELF_IMPROVEMENT_CYCLE_COMPLETED",
            source="SelfImprovementServiceLayer",
            payload={
                "pipeline_id": str(pipeline.pipeline_id),
                "evolved": evo_dict["evolved"],
                "version": evo_dict["version"],
                "success_ratio": ana_dict["success_ratio"],
            },
        )
        if evo_dict["evolved"]:
            self.event_bus.publish(
                event_type="BRAIN_EVOLUTION_APPLIED",
                source="BrainEvolutionManager",
                payload={
                    "pipeline_id": str(pipeline.pipeline_id),
                    "version": evo_dict["version"],
                    "summary": evo_dict["evolution_summary"],
                },
            )
            self.workflow_events.emit(
                workflow_id=pipeline.pipeline_id,
                state="EVOLVED",
                step=len(agents),
                payload={"version": evo_dict["version"], "summary": evo_dict["evolution_summary"]},
            )

        plat_summary = self.platform_srv.get_platform_summary()
        current_context.metadata["platform_report"] = plat_summary
        context.metadata["platform_report"] = plat_summary

        cfg_dict = plat_summary["configuration"]
        db_dict = plat_summary["database"]
        dep_dict = plat_summary["deployment"]

        print("\n" + "=" * 75)
        print(f"[PLATFORM FINALIZATION] Status: {plat_summary['status']} | Env: {cfg_dict['environment']} | DB Connected: {db_dict['connected']}")
        print(f"[DEPLOYMENT PACKAGE] Version: {dep_dict['app_version']} | Docker Image: {dep_dict['docker_image']} | Manifest: {dep_dict['kubernetes_manifest']}")
        print("=" * 75)

        self.event_bus.publish(
            event_type="PLATFORM_DEPLOYABILITY_VERIFIED",
            source="PlatformFinalizationService",
            payload={
                "pipeline_id": str(pipeline.pipeline_id),
                "status": plat_summary["status"],
                "version": dep_dict["app_version"],
                "environment": cfg_dict["environment"],
            },
        )

        rel_summary = self.release_srv.get_release_summary()
        current_context.metadata["production_release_report"] = rel_summary
        context.metadata["production_release_report"] = rel_summary

        print("\n" + "=" * 75)
        print(f"[PRODUCTION FREEZE V1.0] Production Ready: {rel_summary['is_production_ready']} | Version: {rel_summary['version']}")
        print(f"[ARCHITECTURE & CONTRACTS] Arch Frozen: {rel_summary['arch_freeze']['is_frozen']} | Contracts Frozen: {rel_summary['contract_freeze']['is_frozen']} | Governance: {rel_summary['governance']['governance_version']}")
        print("=" * 75)

        self.event_bus.publish(
            event_type="PRODUCTION_RELEASE_VERIFIED",
            source="ProductionReleaseService",
            payload={
                "pipeline_id": str(pipeline.pipeline_id),
                "ready": rel_summary["is_production_ready"],
                "version": rel_summary["version"],
                "arch_frozen": rel_summary["arch_freeze"]["is_frozen"],
                "contracts_frozen": rel_summary["contract_freeze"]["is_frozen"],
            },
        )
        self.workflow_events.emit(
            workflow_id=pipeline.pipeline_id,
            state="FROZEN_V1_0",
            step=len(agents),
            payload={
                "version": rel_summary["version"],
                "ready": rel_summary["is_production_ready"],
            },
        )

        # 2. Emit Workflow Event & Publish EventBus for Pipeline Completion (8.1 & 8.3)
        self.workflow_events.emit(
            workflow_id=pipeline.pipeline_id,
            state="COMPLETED",
            step=len(agents),
            payload={"results_count": len(results), "success": agg_pkg.success},
        )
        self.event_bus.publish(
            event_type="PIPELINE_COMPLETED",
            source="AgentOrchestrator",
            payload={"pipeline_id": str(pipeline.pipeline_id), "success": agg_pkg.success},
        )

        current_context.metadata["aggregated_result_package"] = agg_pkg
        current_context.metadata["orchestration_metrics"] = metrics
        current_context.metadata["event_bus_metrics"] = self.event_bus.monitor.get_metrics()
        current_context.metadata["workflow_events_history"] = len(self.workflow_events.tracker.get_history(pipeline.pipeline_id))

        print("\n" + "=" * 75)
        print(f"[ORCHESTRATOR COMPLETE] Finished Pipeline Execution ({len(results)} results)")
        print(f"[MONITORING] Bottleneck Detected: {metrics.bottleneck_report.has_bottleneck} | Total Duration: {metrics.pipeline_summary.total_duration_ms:.2f}ms")
        print(f"[COMMUNICATION] EventBus Delivered: {self.event_bus.monitor.get_metrics().delivered_count} events | Workflow History: {len(self.workflow_events.tracker.get_history(pipeline.pipeline_id))} events")
        print("=" * 75)

        return results

    def _merge_result_context(
        self,
        context: AgentExecutionContext,
        result: AgentResult,
    ) -> AgentExecutionContext:
        """
        Transfer agent output into next agent context.
        """

        metadata = dict(context.metadata)

        metadata["agent_results"] = {
            **metadata.get(
                "agent_results",
                {},
            ),
            result.data.get(
                "agent",
                "unknown",
            ): result.data,
        }

        if "architecture_plan" in result.data:
            metadata["architecture_plan"] = result.data["architecture_plan"]
        if "research_report" in result.data:
            metadata["research_report"] = result.data["research_report"]
        if "project_vision" in result.data:
            metadata["project_vision"] = result.data["project_vision"]

        return replace(
            context,
            metadata=metadata,
        )

    def _needs_retry(
        self,
        results: Sequence[AgentResult],
    ) -> bool:
        """
        Determine whether iteration should be retried.
        """

        for result in results:
            if not result.success:
                return True

        return False
