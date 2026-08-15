"""
ShadBot Agent Platform

Unified service for Phase 11 Platform Finalization.
"""

from __future__ import annotations

from uuid import uuid4
from .api_layer import APIRequest, APIResponse, PlatformAPIGateway
from .configuration import ConfigurationManager, PlatformConfigPackage
from .database_integration import DatabaseConnectionReport, EnterpriseDatabaseAdapter
from .deployment import DeploymentManager, DeploymentPackage
from .logging_system import EnterpriseLogger
from .plugin_architecture import PluginManager


class PlatformFinalizationService:
    """
    Orchestrates API Gateway, Configuration, Logging, Database, Plugins, and Deployment architecture.
    """

    def __init__(self) -> None:
        self.config_mgr = ConfigurationManager()
        self.logger = EnterpriseLogger()
        self.api_gw = PlatformAPIGateway()
        self.db_adapter = EnterpriseDatabaseAdapter()
        self.plugin_mgr = PluginManager()
        self.deploy_mgr = DeploymentManager()

    def finalize_platform(self) -> tuple[PlatformConfigPackage, DatabaseConnectionReport, DeploymentPackage]:
        cfg = self.config_mgr.get_config()
        self.logger.log("INFO", "Configuration loaded successfully")
        db = self.db_adapter.connect()
        self.logger.log("INFO", f"Connected to {db.database_name}")
        self.plugin_mgr.load_plugin("EnterpriseMetricsPlugin")
        pkg = self.deploy_mgr.build_package()
        return cfg, db, pkg

    def get_platform_summary(self) -> dict[str, object]:
        cfg, db, pkg = self.finalize_platform()
        plugins = [p.to_dict() for p in self.plugin_mgr.list_plugins()]
        logs = [l.to_dict() for l in self.logger.get_records()]
        return {
            "configuration": cfg.to_dict(),
            "database": db.to_dict(),
            "deployment": pkg.to_dict(),
            "plugins": plugins,
            "logs": logs,
            "status": "DEPLOYABLE",
        }
