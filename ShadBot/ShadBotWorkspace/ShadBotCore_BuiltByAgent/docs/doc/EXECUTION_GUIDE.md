\# ShadBot Agent Platform

\# Execution Guide



Version: 1.0



Status: Official Runtime Execution Guide



\---



\# Purpose



This document explains exactly how the completed Agent Platform is expected to run in production.



It is the operational guide for anyone (human or AI) who wants to execute the platform.



After Phase 12, this document becomes the primary execution reference.



\---



\# Overall Execution Lifecycle



```text

Start Platform

&#x20;       │

&#x20;       ▼

Load Configuration

&#x20;       │

&#x20;       ▼

Bootstrap Platform

&#x20;       │

&#x20;       ▼

Initialize Brain

&#x20;       │

&#x20;       ▼

Initialize Runtime

&#x20;       │

&#x20;       ▼

Discover Project Workspace

&#x20;       │

&#x20;       ▼

Read task.md

&#x20;       │

&#x20;       ▼

Execute Brain Cycle

&#x20;       │

&#x20;       ▼

Coordinate Agents

&#x20;       │

&#x20;       ▼

Validate Output

&#x20;       │

&#x20;       ▼

Reflect

&#x20;       │

&#x20;       ▼

Learn

&#x20;       │

&#x20;       ▼

Update task status

&#x20;       │

&#x20;       ▼

Generate report

&#x20;       │

&#x20;       ▼

Idle / Wait for next task

```



\---



\# Project Workspace Layout



Every product built by the platform must follow this layout:



```text

MyProject/



├── Source/



├── Docs/



├── Reports/



├── Tests/



├── Config/



└── Tasks/



&#x20;     └── task.md

```



The platform never starts from source code.



It always starts from:



```

Tasks/task.md

```



\---



\# Task File



Example



```markdown

\# Goal



Build authentication module.



\## Requirements



\- JWT

\- Refresh token

\- SQL Server

\- Unit tests

\- API



\## Constraints



\- Enterprise grade

\- No placeholders

\- Production ready

```



\---



\# Startup Sequence



1\.



Load configuration.



↓



2\.



Initialize Dependency Injection.



↓



3\.



Create Brain Runtime.



↓



4\.



Load Memory.



↓



5\.



Load Agent Profiles.



↓



6\.



Load Capabilities.



↓



7\.



Initialize Event Bus.



↓



8\.



Initialize Runtime.



↓



9\.



Wait for Project Workspace.



\---



\# Workspace Discovery



Brain searches for



```

Tasks/task.md

```



If not found



↓



Idle



If found



↓



Task Intake



\---



\# Brain Cycle



For every task



Brain executes



```text

Goal Execution



↓



Context Assembly



↓



Memory Retrieval



↓



Workspace Observation



↓



Reasoning



↓



Decision



↓



Planning



↓



Agent Assignment

```



Output



Execution Plan



\---



\# Agent Execution



Execution Plan



↓



Agent Orchestrator



↓



Agent Selection



↓



Pipeline



↓



Execution



↓



Result Aggregation



↓



Runtime



\---



\# Runtime



Runtime manages



\- execution state

\- checkpoints

\- resume

\- async execution

\- failures



Runtime never performs reasoning.



\---



\# Validation



After execution



Automatically run



```text

pytest



↓



ruff



↓



black



↓



mypy



↓



Security Validation



↓



Architecture Validation

```



\---



\# If Validation Fails



```text

Validation



↓



Reflection



↓



Failure Analysis



↓



Improvement Proposal



↓



Execution



↓



Validation

```



Loop until PASS.



\---



\# Reflection



Reflection produces



\- review

\- mistakes

\- improvements



Reflection never modifies code directly.



It sends improvements back into the Brain.



\---



\# Learning



Learning stores



\- experience

\- patterns

\- successful strategies

\- failed strategies



Memory updated



Brain evolves



\---



\# Task Completion



When every validation succeeds



Update



```

Tasks/task.md

```



Status



Completed



Generate



```

Reports/



Artifacts/



Logs/



Summary

```



\---



\# Completion Report



Minimum report



```text

Task



Start Time



End Time



Duration



Agents Used



Files Created



Files Modified



Validation Status



Reflection Summary



Learning Summary

```



\---



\# Failure Report



If execution cannot recover



Generate



```text

Failure Cause



Reasoning Trace



Attempt History



Validation Errors



Recommended Next Action

```



\---



\# Automatic Product Workflow



Normal production workflow



```text

Create Workspace



↓



Write task.md



↓



Run Platform



↓



Platform builds product



↓



Platform validates product



↓



Platform learns



↓



Platform reports completion



↓



Wait for next task

```



No manual orchestration required.



\---



\# Running the Platform



Expected production command



```powershell

python run.py

```



The platform should:



\- initialize itself

\- discover workspaces

\- execute queued tasks

\- wait for additional tasks



\---



\# Running a Specific Project



Expected command



```powershell

python run.py --workspace Projects/MyProject

```



or



```powershell

python run.py --project MyProject

```



The runtime resolves the workspace, loads its task queue, and begins execution.



\---



\# Idle Mode



If no task exists



Platform remains alive.



It periodically scans configured workspaces.



When a new task appears



Execution starts automatically.



\---



\# Shutdown



Graceful shutdown sequence



```text

Stop accepting new tasks



↓



Finish current checkpoint



↓



Persist runtime state



↓



Persist memory updates



↓



Persist session



↓



Shutdown

```



No work should be lost.



\---



\# Resume



After restart



Platform restores



\- runtime

\- checkpoints

\- session

\- unfinished tasks



Execution resumes from the last checkpoint instead of restarting.



\---



\# Production Definition



Platform V1.0 is considered production-ready only when it can:



\- bootstrap successfully

\- discover workspaces

\- execute task.md autonomously

\- coordinate agents

\- recover from failures

\- pass all quality gates

\- learn from execution

\- generate completion reports

\- resume interrupted executions

\- wait for the next task without human intervention



When these conditions are satisfied, the Agent Platform is complete and future work shifts entirely to building products through Project Workspaces.

