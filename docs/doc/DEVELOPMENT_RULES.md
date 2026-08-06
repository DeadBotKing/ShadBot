\# ShadBot Agent Platform

\# Development Rules



Version: 1.0



Status: Official Development Standard



\---



\# Purpose



This document defines the mandatory engineering rules for every developer, AI agent, and contributor working on the ShadBot Agent Platform.



These rules are mandatory.



Violation of these rules is considered an implementation error.



\---



\# Rule 1 — Architecture



The platform follows \*\*Clean Architecture\*\*.



Dependency direction is always:



```

Presentation

&#x20;       ↓

Application

&#x20;       ↓

Domain

&#x20;       ↓

Infrastructure (implements contracts only)

```



Never reverse this dependency.



\---



\# Rule 2 — Domain First



Business logic belongs only inside Domain.



Never place business logic inside:



\- Infrastructure

\- Presentation

\- API

\- Runtime



\---



\# Rule 3 — Contracts First



Every communication between modules must happen through Contracts.



Never call Infrastructure directly.



Correct:



```

Application

&#x20;     ↓

Contract

&#x20;     ↓

Infrastructure

```



Wrong:



```

Application

&#x20;     ↓

Infrastructure

```



\---



\# Rule 4 — Single Responsibility



Every class has one responsibility.



Every service has one responsibility.



Every module has one responsibility.



Large classes must be decomposed.



\---



\# Rule 5 — Dependency Injection



Never instantiate dependencies directly.



Use dependency injection everywhere.



Wrong



```python

MemoryRepository()

```



Correct



```python

memory\_repository: MemoryRepository

```



\---



\# Rule 6 — No Hidden State



Every execution state must be explicit.



No hidden globals.



No singleton state.



No implicit mutable objects.



\---



\# Rule 7 — Stateless Application Layer



Application services must remain stateless.



Runtime state belongs inside Runtime System.



\---



\# Rule 8 — Memory Ownership



Only Memory Flow manages memory.



Agents never write directly into storage.



Agents request memory updates through contracts.



\---



\# Rule 9 — Workspace Ownership



Only Eye Flow may observe the Project Workspace.



Agents never scan the filesystem directly.



\---



\# Rule 10 — Brain Ownership



Only Brain Orchestrator performs:



\- reasoning

\- planning

\- decisions



Agents execute.



Brain thinks.



\---



\# Rule 11 — Task Ownership



Every execution starts from



```

Project Workspace/

└── Tasks/

&#x20;   └── task.md

```



Nothing else starts execution.



\---



\# Rule 12 — Validation Before Completion



A task is never considered complete until every quality gate passes.



Required gates:



\- pytest

\- ruff

\- black

\- mypy

\- security validation

\- architecture validation



\---



\# Rule 13 — Automatic Fix Loop



If validation fails:



```

Execution

&#x20;     ↓

Validation

&#x20;     ↓

Failure

&#x20;     ↓

Reflection

&#x20;     ↓

Fix

&#x20;     ↓

Validation

```



Repeat until success.



\---



\# Rule 14 — Reflection



Every execution must generate:



\- execution review

\- failure analysis

\- lessons learned



Reflection is mandatory.



\---



\# Rule 15 — Learning



Every successful execution updates:



\- memory

\- knowledge

\- strategy



The platform continuously improves.



\---



\# Rule 16 — Logging



Every important action must be logged.



Minimum events:



\- task started

\- reasoning started

\- decision produced

\- execution started

\- validation finished

\- task completed

\- task failed



\---



\# Rule 17 — Configuration



Never hardcode:



\- paths

\- API keys

\- database strings

\- model names

\- runtime parameters



Everything must come from configuration.



\---



\# Rule 18 — Error Handling



Never ignore exceptions.



Never use bare:



```python

except:

```



Always raise meaningful exceptions.



Always preserve stack traces.



\---



\# Rule 19 — Async Safety



Long-running work must be asynchronous.



Never block the Brain.



Never block Runtime.



\---



\# Rule 20 — Deterministic Planning



Planning must always produce the same plan given identical:



\- Goal

\- Context

\- Memory



Planning must be reproducible.



\---



\# Rule 21 — Agent Isolation



Agents never call each other directly.



Communication always goes through:



\- Orchestrator

\- Event Bus

\- Messaging Layer



\---



\# Rule 22 — Runtime Recovery



Every execution must support:



\- checkpoint

\- resume

\- recovery



Unexpected shutdowns must not destroy progress.



\---



\# Rule 23 — No Duplicate Logic



Never duplicate business logic.



Extract shared behavior into reusable services.



\---



\# Rule 24 — Naming Convention



Python



\- snake\_case for files

\- PascalCase for classes

\- snake\_case for functions

\- UPPER\_CASE for constants



Folders



\- lowercase\_with\_underscores



\---



\# Rule 25 — Documentation



Every public module must contain:



\- purpose

\- responsibility

\- dependencies

\- outputs



Public classes and services require docstrings.



\---



\# Rule 26 — Testing



Every production module requires tests.



Minimum:



\- unit tests

\- integration tests (where applicable)



Production code without tests is incomplete.



\---



\# Rule 27 — Enterprise Quality



Generated code must be:



\- production-ready

\- enterprise-grade

\- modular

\- testable

\- extensible



Never generate:



\- placeholder code

\- TODO blocks

\- fake implementations

\- temporary hacks

\- demo code

\- mock business logic



\---



\# Rule 28 — Platform Freeze



After Phase 12:



The Agent Platform architecture is frozen.



Only Product Workspaces evolve.



Platform changes require a new architecture version.



\---



\# Rule 29 — Product Development



After Freeze V1.0 the workflow is:



```

Create Project Workspace



↓



Write task.md



↓



Run Platform



↓



Platform builds product



↓



Quality Gate



↓



Completion Report

```



No manual orchestration is required.



\---



\# Rule 30 — Ultimate Principle



The Brain decides.



The Orchestrator coordinates.



The Runtime executes.



The Agents build.



The Quality Gate verifies.



The Learning System improves.



No component may violate this separation of responsibilities.

