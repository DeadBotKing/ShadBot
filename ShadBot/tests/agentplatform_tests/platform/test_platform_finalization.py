"""
ShadBot Agent Platform

Unit tests for Phase 11 Platform Finalization.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.application.platform import (
    APIRequest,
    APIResponse,
    ConfigurationManager,
    EnterpriseDatabaseAdapter,
    EnterpriseLogger,
    LoadedPlugin,
    PlatformAPIGateway,
    PlatformConfigPackage,
    PlatformFinalizationService,
    PluginManager,
)
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult


def test_configuration_manager_loads_defaults() -> None:
    cfg = ConfigurationManager().get_config("production")
    assert cfg.environment == "production"
    assert cfg.default_llm_model == "qwen3-coder-next:latest"


def test_enterprise_logger_records_records() -> None:
    logger = EnterpriseLogger()
    rec = logger.log("INFO", "Platform started")
    assert rec.level == "INFO"
    assert len(logger.get_records()) == 1


def test_api_gateway_handles_request() -> None:
    gw = PlatformAPIGateway()
    req = APIRequest("/api/v1/tasks/execute", "POST", {}, uuid4())
    res = gw.handle_request(req)
    assert res.status_code == 202
    assert res.body["status"] == "ACCEPTED"


def test_platform_finalization_service_orchestrates() -> None:
    service = PlatformFinalizationService()
    cfg, db, pkg = service.finalize_platform()
    assert cfg.environment == "production"
    assert db.connected is True
    assert "shadbot-agent-platform" in pkg.docker_image


def test_platform_models_to_dict() -> None:
    rid = uuid4()
    req = APIRequest("/test", "GET", {}, rid)
    res = APIResponse(rid, 200, {"status": "ok"})
    cfg = ConfigurationManager().get_config()
    db = EnterpriseDatabaseAdapter().connect()
    logger = EnterpriseLogger()
    log_rec = logger.log("INFO", "test log")
    plg = LoadedPlugin("TestPlugin", "1.0", True)

    assert isinstance(req.to_dict(), dict) and req.to_dict()["request_id"] == str(rid)
    assert isinstance(res.to_dict(), dict) and res.to_dict()["request_id"] == str(rid)
    assert isinstance(cfg.to_dict(), dict) and cfg.to_dict()["environment"] == "production"
    assert isinstance(db.to_dict(), dict) and db.to_dict()["connected"] is True
    assert isinstance(log_rec.to_dict(), dict) and log_rec.to_dict()["level"] == "INFO"
    assert isinstance(plg.to_dict(), dict) and plg.to_dict()["enabled"] is True


def test_platform_service_get_platform_summary() -> None:
    service = PlatformFinalizationService()
    summary = service.get_platform_summary()
    assert isinstance(summary, dict)
    assert summary["status"] == "DEPLOYABLE"
    assert "configuration" in summary
    assert "database" in summary
    assert "deployment" in summary
    assert "plugins" in summary
    assert "logs" in summary


class FakeAgent:
    name = "architect"

    def run(self, context: AgentExecutionContext):
        return AgentResult(
            success=True,
            message="Architecture completed.",
            data={"agent": "architect", "architecture_plan": "plan"},
        )


class FakeExecutionService:
    def execute(self, agent, context):
        return agent.run(context)


def test_orchestrator_integrates_platform_finalization() -> None:
    orchestrator = AgentOrchestrator(execution_service=FakeExecutionService())  # type: ignore[arg-type]
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Test Platform Finalization in Orchestrator",
        task_title="Test Task",
        metadata={},
    )
    results = orchestrator.execute_pipeline([FakeAgent()], context)  # type: ignore[list-item]
    assert len(results) == 1
    assert "platform_report" in context.metadata
    report = context.metadata["platform_report"]
    assert report["status"] == "DEPLOYABLE"
    assert report["database"]["connected"] is True

