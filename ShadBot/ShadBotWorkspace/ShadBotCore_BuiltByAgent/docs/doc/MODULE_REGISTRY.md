\# ShadBot Agent Platform

\# Module Registry



Version: 1.0



Status: Active Development





\# 1. Purpose



This document is the official registry of all ShadBot Agent Platform modules.



Every module must have:



\- Defined responsibility

\- Clear ownership

\- Dependency direction

\- Implementation status

\- Integration status





The registry prevents:



\- Duplicate modules

\- Architecture drift

\- Broken dependencies

\- Unknown ownership





\---



\# 2. Architecture Overview



agentplatform



├── domain



├── application



├── infrastructure



└── presentation







Dependency direction:



Presentation

&#x20;   ↓

Application

&#x20;   ↓

Domain

&#x20;   ↓

Infrastructure

&#x20;   ↓

Application + Domain Contracts







Rules:



\- Domain never depends on other layers.

\- Application contains business workflows.

\- Infrastructure implements contracts.

\- Presentation exposes interfaces.





\---



\# 3. Domain Modules Registry





\## 3.1 Agent Domain





Path:

src/agentplatform/domain/agents







Responsibility:



Agent identity and lifecycle definitions.





Status:



COMPLETE





Contains:



\- Agent entities

\- Agent models

\- Agent contracts







\---



\## 3.2 Capability Domain





Path:







src/agentplatform/domain/capabilities









Responsibility:



Define what agents can do.





Status:



COMPLETE





Contains:



\- Capability models

\- Capability contracts







\---



\## 3.3 Tool Domain





Path:

src/agentplatform/domain/tools







Responsibility:



Tool definition and execution contracts.





Status:



COMPLETE







\---



\## 3.4 Task Domain





Path:

src/agentplatform/domain/tasks







Responsibility:



Task representation and lifecycle.





Status:



COMPLETE







\---



\## 3.5 Memory Domain





Path:

src/agentplatform/domain/memory







Responsibility:



Memory entities and contracts.





Status:



PARTIAL





Current blocker:





Missing:

MemoryEntry







Required:



Complete exports and domain contracts.





\---



\## 3.6 Goal Domain





Path:



src/agentplatform/domain/goal







Responsibility:



Goal lifecycle management.





Status:



FOUNDATION COMPLETE







\---



\## 3.7 Context Domain





Path:

src/agentplatform/domain/context







Responsibility:



Context representation.





Status:



FOUNDATION COMPLETE







\---



\## 3.8 Decision Domain





Path:

src/agentplatform/domain/decision







Responsibility:



Decision models and outputs.





Status:



FOUNDATION COMPLETE







\---



\## 3.9 Planning Domain





Path:

src/agentplatform/domain/planning







Responsibility:



Execution planning structures.





Status:



FOUNDATION COMPLETE







\---



\## 3.10 Validation Domain





Path:

src/agentplatform/domain/validation







Responsibility:



Validation models and rules.





Status:



FOUNDATION COMPLETE







\---



\# 4. Application Modules Registry





\## 4.1 Agent Management





Path:

application/agents







Status:



COMPLETE





Responsibility:



Agent execution logic.







\---



\## 4.2 Brain Orchestrator





Path:

application/brain







Status:



IN PROGRESS





Responsibility:



Central cognitive orchestration layer.





Contains:



brain



├── goal



├── context



├── memory



├── eye\_flow



├── reasoning



├── decision



├── planning



├── reflection



├── learning



└── attention







\---



\## 4.3 Goal System





Path:

application/goal







Status:



FOUNDATION COMPLETE





Responsibility:



Goal intake, tracking and completion.







\---



\## 4.4 Context System





Path:

application/context







Status:



FOUNDATION COMPLETE





Responsibility:



Context collection and management.







\---



\## 4.5 Memory System





Path:

application/memory







Status:



PARTIAL





Responsibility:



Memory retrieval, ranking, injection and update.







\---



\## 4.6 Execution System





Path:

application/execution







Status:



COMPLETE





Responsibility:



Agent execution workflow.







\---



\## 4.7 Orchestration System





Path:

application/orchestration







Status:



FOUNDATION COMPLETE





Responsibility:



Coordinate agent workflows.







\---



\## 4.8 Task Management





Path:

application/tasks

application/task\_manager







Status:



FOUNDATION COMPLETE





Responsibility:



Task lifecycle handling.







\---



\## 4.9 Runtime System





Path:

application/runtime







Status:



FOUNDATION COMPLETE





Responsibility:



Runtime execution management.







\---



\## 4.10 Validation System





Path:

application/validation







Status:



FOUNDATION COMPLETE





Responsibility:



Quality and output validation.







\---



\## 4.11 Learning System





Path:

application/learning







Status:



FOUNDATION COMPLETE





Responsibility:



Learning and improvement workflows.







\---



\## 4.12 Improvement System





Path:

application/improvement







Status:



FOUNDATION COMPLETE





Responsibility:



Self improvement mechanisms.







\---



\# 5. Infrastructure Modules Registry





\## 5.1 Agent Infrastructure





Path:

infrastructure/agents







Status:



COMPLETE





Responsibility:



Agent implementations and adapters.







\---



\## 5.2 Memory Infrastructure





Path:

infrastructure/memory







Status:



PARTIAL





Contains:



\- JSON Memory Repository





Blocked by:



Memory Domain completion.







\---



\## 5.3 LLM Infrastructure





Path:

infrastructure/llm







Status:



FOUNDATION COMPLETE





Responsibility:



LLM provider abstraction.







\---



\## 5.4 Registration Infrastructure





Path:

infrastructure/registration







Status:



FOUNDATION COMPLETE





Responsibility:



Agent and service registration.







\---



\## 5.5 Tool Infrastructure





Path:

infrastructure/tools







Status:



FOUNDATION COMPLETE





Responsibility:



Tool execution adapters.







\---



\## 5.6 Runtime Infrastructure





Path:

infrastructure/brain







Status:



FOUNDATION COMPLETE





Responsibility:



Infrastructure support for brain execution.







\---



\# 6. Agent Registry





| Agent | Status | Responsibility |

|-|-|-|

| Architect Agent | Implemented | Architecture design |

| Researcher Agent | Implemented | Research and knowledge |

| Reviewer Agent | Implemented | Review and validation |

| Project Intelligence Agent | Foundation | Workspace/project understanding |





\---



\# 7. Core Flow Registry





Current execution direction:

Task



↓



Goal Intake



↓



Context Assembly



↓



Memory Retrieval



↓



Eye Observation



↓



Reasoning



↓



Decision



↓



Planning



↓



Agent Execution



↓



Validation



↓



Reflection



↓



Learning Update







\---



\# 8. Future Phase Ownership





\## Phase 5



Owned modules:

application/brain







\---



\## Phase 6



Owned modules:

application/orchestration

application/dispatch

application/workflow







\---



\## Phase 7



Owned modules:

application/runtime

infrastructure/runtime







\---



\## Phase 8



Owned modules:

events

communication

workflow events







\---



\## Phase 9



Owned modules:

validation

testing

quality gates







\---



\## Phase 10



Owned modules:

improvement

learning

experiments







\---



\## Phase 11



Owned modules:

configuration

logging

database

plugins

deployment









\---



\## Phase 12



Owned modules:

integration

release

freeze







\---



\# 9. Registry Rules





Every new module must define:





1\. Purpose



2\. Layer ownership



3\. Contracts



4\. Dependencies



5\. Tests



6\. Integration point







No module is considered complete without:





\- Implementation

\- Tests

\- Contract registration

\- Documentation





\---



\# 10. Current Registry Status





Total Architecture Modules:



Registered





Implementation:



Foundation complete





Current Development Phase:

Phase 5 — Brain Orchestrator





Current Blocker:

MemoryEntry domain completion





End of Registry.



