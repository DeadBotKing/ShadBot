\# ShadBot Agent Platform

\# Architecture Handoff Document

\# Version: 1.0





\# 1. Architecture Overview





ShadBot Agent Platform is an enterprise autonomous AI engineering platform.



The architecture is designed to allow AI agents to understand, plan, execute, validate, and improve software projects autonomously.





Core architectural principles:



\- Clean Architecture

\- Domain Driven Design

\- Modular Agents

\- Contract Based Communication

\- Dependency Inversion

\- Event Driven Execution

\- Autonomous Workflow Management





\---



\# 2. High Level Architecture



&#x20;               User



&#x20;                |



&#x20;         Task Workspace



&#x20;                |



&#x20;            Brain Layer



&#x20;                |



&#x20;     Agent Orchestration Layer



&#x20;                |



&#x20;         Agent Runtime



&#x20;                |



&#x20;         Agent Execution



&#x20;                |



&#x20;        Quality Gate System



&#x20;                |



&#x20;         Product Output







\---



\# 3. Core System Layers





\## 3.1 Domain Layer





Location:



src/agentplatform/domain







Responsibility:



Contains core business logic and contracts.





Contains:



\- Agent entities

\- Task entities

\- Goal models

\- Memory models

\- Capability models

\- Execution models

\- Event models

\- Validation models





Rules:



\- No infrastructure dependency.

\- No framework dependency.

\- Pure business logic only.





\---



\# 3.2 Application Layer





Location:



src/agentplatform/application







Responsibility:



Coordinates system behavior.





Contains:



application/



├── agents



├── brain



├── capabilities



├── execution



├── orchestration



├── planning



├── reasoning



├── decision



├── memory



├── validation



├── runtime



├── workflow



├── tools



└── workspace







\---



\# 3.3 Infrastructure Layer





Location:



src/agentplatform/infrastructure







Responsibility:



Provides technical implementations.





Contains:





\- Persistence

\- Tool adapters

\- LLM adapters

\- Runtime services

\- External integrations





\---



\# 4. Agent Architecture





Agents are autonomous execution units.





Each agent contains:



Agent



├── Profile



├── Capabilities



├── Tools



├── Memory Access



├── Reasoning Ability



├── Execution Ability



└── Validation Rules







\---



\# 5. Core Agents





\## 5.1 Architect Agent





Responsibility:



\- Analyze architecture

\- Design solutions

\- Create technical plans

\- Define implementation strategy





\---



\## 5.2 Researcher Agent





Responsibility:



\- Gather technical information

\- Analyze technologies

\- Provide knowledge





\---



\## 5.3 Project Intelligence Agent





IMPORTANT:



Project Intelligence is NOT a separate project anymore.



All project understanding capabilities are implemented inside this agent.





Responsibility:





Understand target project workspace.





Capabilities:





\### Workspace Understanding



\- Scan project files

\- Understand directory structure

\- Detect technologies

\- Analyze project state





\### Snapshot Capability



\- Create project snapshots

\- Compare changes

\- Track evolution





\### Knowledge Extraction



\- Extract project facts

\- Understand conventions

\- Detect architecture patterns





\### Dependency Analysis



\- Analyze dependencies

\- Detect relationships





\### Git Understanding



\- Read repository status

\- Analyze history

\- Detect changes





\### Context Generation



Provide project context to Brain Orchestrator.





Flow:



Project Workspace



↓



Project Intelligence Agent



↓



Project Understanding Context



↓



Brain Orchestrator







\---



\## 5.4 Engineer Agents





Responsibility:





\- Generate code

\- Modify code

\- Implement features

\- Fix issues





\---



\## 5.5 Reviewer Agent





Responsibility:





\- Review implementation

\- Detect problems

\- Suggest improvements





\---



\# 6. Brain Architecture





The Brain is the central intelligence system.





Location:



src/agentplatform/application/brain







Responsibilities:





\- Understand goals

\- Manage context

\- Retrieve memory

\- Reason

\- Decide

\- Plan

\- Reflect

\- Learn





Architecture:



Brain Orchestrator



├── Goal Flow



├── Context Flow



├── Memory Flow



├── Eye Flow



├── Reasoning Flow



├── Decision Flow



├── Profile Flow



├── Planning Flow



├── Reflection Flow



├── Validation Flow



├── Learning Flow



├── Intent Flow



└── Attention Flow







\---



\# 7. Task Driven Architecture





The platform is controlled by project tasks.





Each project workspace contains:



Project Workspace



└── Tasks

└── task.md





Task lifecycle:

task.md



↓



Task Intake Layer



↓



Goal Creation



↓



Brain Understanding



↓



Planning



↓



Agent Execution



↓



Validation



↓



Completion Report









\---



\# 8. Execution Architecture





Execution pipeline:



Task



↓



Goal



↓



Context Assembly



↓



Plan Generation



↓



Agent Selection



↓



Agent Execution



↓



Result Collection



↓



Quality Gate



↓



Completion Detection







\---



\# 9. Communication Architecture





Agents communicate through:





\- Event Bus

\- Agent Messaging

\- Workflow Events

\- Async Execution





Flow:



Agent A



↓



Event Bus



↓



Agent B







\---



\# 10. Memory Architecture





Memory system provides:





\- Experience storage

\- Context retrieval

\- Previous execution knowledge

\- Improvement history





Flow:



Execution



↓



Memory Update



↓



Future Retrieval



↓



Brain Injection







\---



\# 11. Quality Architecture





Every generated result must pass:



Pytest



↓



Ruff



↓



Black



↓



MyPy



↓



Security Validation



↓



Architecture Validation







Failure:



Return to Brain for correction loop.





\---



\# 12. Final Autonomous Workflow





Final expected behavior:



User



↓



Creates Project Workspace



↓



Adds task.md



↓



Runs:



python run.py ProjectName



↓



Platform starts



↓



Project Intelligence Agent understands project



↓



Brain creates execution strategy



↓



Agents build product



↓



Quality Gate validates



↓



System reports completion







\---



\# 13. Architectural Freeze Rules





Future developers must:



\- Do not create independent Project Intelligence project.

\- Extend Project Intelligence Agent instead.

\- Preserve contracts.

\- Avoid breaking existing layers.

\- Add capabilities through agents and tools.

\- Keep Brain independent from infrastructure.





This document defines the official ShadBot Agent Platform architecture.

