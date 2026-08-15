\# ShadBot Agent Platform

\# Data Flow Documentation



Version: 1.0



Status: Official Data Flow Specification



\---



\# Purpose



This document defines how data flows through the entire Agent Platform.



It is the single source of truth for execution flow.



Every module implemented in the platform must follow these flows.



No module may invent its own execution path.



\---



\# Global Execution Flow



```text

Project Workspace

&#x20;       │

&#x20;       ▼

Tasks/task.md

&#x20;       │

&#x20;       ▼

Task Intake Layer

&#x20;       │

&#x20;       ▼

Goal Execution

&#x20;       │

&#x20;       ▼

Context Assembly

&#x20;       │

&#x20;       ▼

Memory Flow

&#x20;       │

&#x20;       ▼

Eye Flow

&#x20;       │

&#x20;       ▼

Reasoning Flow

&#x20;       │

&#x20;       ▼

Decision Flow

&#x20;       │

&#x20;       ▼

Planning Flow

&#x20;       │

&#x20;       ▼

Agent Orchestration

&#x20;       │

&#x20;       ▼

Runtime System

&#x20;       │

&#x20;       ▼

Communication Layer

&#x20;       │

&#x20;       ▼

Quality Gate System

&#x20;       │

&#x20;       ▼

Reflection Flow

&#x20;       │

&#x20;       ▼

Learning Flow

&#x20;       │

&#x20;       ▼

Brain Evolution

&#x20;       │

&#x20;       ▼

Task Completion

```



\---



\# Stage 1

Project Workspace



Input



```

Project Workspace



├── Source Code



├── Documents



├── Tasks



│      └── task.md



├── Reports



├── Tests



└── Config

```



Output



Raw Task



\---



\# Stage 2

Task Intake Layer



Receives



task.md



Produces



Normalized Task



Responsibilities



\- Discover Project Workspace

\- Read task file

\- Parse Markdown

\- Normalize structure

\- Register execution state



Output



Task Object



\---



\# Stage 3

Goal Execution



Input



Task



Produces



Goal



Goal Intent



Goal State



Responsibilities



\- Understand objective

\- Detect completion criteria

\- Build lifecycle



Output



Goal Object



\---



\# Stage 4

Context Assembly



Input



Goal



Collects



Workspace



Memory



Environment



Runtime



Agent Profile



Project State



Produces



Context Snapshot



Responsibilities



\- Collect

\- Merge

\- Prioritize

\- Freeze snapshot



Output



Immutable Context



\---



\# Stage 5

Memory Flow



Input



Context



Retrieves



Long-term Memory



Short-term Memory



Session Memory



Experience



Knowledge



Ranks



Most Relevant



Injects



Reasoning Context



Updates



Memory Store



Output



Working Memory



\---



\# Stage 6

Eye Flow



Input



Project Workspace



Observes



Files



Directories



Git



Artifacts



Tests



Reports



Project Status



Environment



Produces



Visual Context



Output



Workspace Understanding



\---



\# Stage 7

Reasoning Flow



Input



Goal



Context



Memory



Workspace



Produces



Problem Analysis



Reasoning



Options



Trade-offs



Reasoning Trace



Output



Reasoning Result



\---



\# Stage 8

Decision Flow



Input



Reasoning Result



Produces



Decision



Execution Strategy



Confidence



Output



Approved Decision



\---



\# Stage 9

Planning Flow



Input



Decision



Produces



Execution Plan



Task Breakdown



Dependencies



Agent Assignment



Execution Order



Output



Execution Plan



\---



\# Stage 10

Agent Orchestration



Input



Execution Plan



Responsibilities



\- Select agents

\- Route tasks

\- Build execution pipeline

\- Manage handoffs

\- Aggregate outputs

\- Recover failures



Output



Executable Work Queue



\---



\# Stage 11

Runtime System



Responsibilities



Execute



Checkpoint



Resume



Persist State



Monitor Session



Output



Execution Result



\---



\# Stage 12

Communication Layer



Responsibilities



Event Bus



Agent Messages



Workflow Events



Async Execution



Output



Coordinated Execution



\---



\# Stage 13

Quality Gate System



Input



Execution Result



Runs



pytest



ruff



black



mypy



Security Validation



Architecture Validation



Decision



PASS



or



FAIL



Output



Validated Result



\---



\# Stage 14

Reflection Flow



Input



Validated Result



Produces



Execution Review



Failure Analysis



Improvement Suggestions



Self Critique



Output



Reflection Report



\---



\# Stage 15

Learning Flow



Input



Reflection



Produces



Experience



Patterns



Knowledge Update



Strategy Improvement



Output



Learning Package



\---



\# Stage 16

Brain Evolution



Input



Learning Package



Produces



Updated Brain State



Improved Strategies



Better Decision Policies



Updated Memory



Output



Evolved Brain



\---



\# Stage 17

Task Completion



Updates



```

Project Workspace



└── Tasks



&#x20;     └── task.md

```



State



Completed



or



Failed



Produces



Completion Report



Execution Summary



Artifacts



Logs



\---



\# Workspace Data Flow



```text

Project Workspace

&#x20;       │

&#x20;       ▼

Tasks/task.md

&#x20;       │

&#x20;       ▼

Task Intake

&#x20;       │

&#x20;       ▼

Brain

&#x20;       │

&#x20;       ▼

Agents

&#x20;       │

&#x20;       ▼

Workspace Modification

&#x20;       │

&#x20;       ▼

Validation

&#x20;       │

&#x20;       ▼

Reports

&#x20;       │

&#x20;       ▼

Learning

```



\---



\# Memory Data Flow



```text

Long Memory

&#x20;     │

&#x20;     ▼

Retrieval

&#x20;     │

&#x20;     ▼

Ranking

&#x20;     │

&#x20;     ▼

Injection

&#x20;     │

&#x20;     ▼

Reasoning

&#x20;     │

&#x20;     ▼

Update

&#x20;     │

&#x20;     ▼

Long Memory

```



\---



\# Context Data Flow



```text

Goal

Workspace

Environment

Memory

Runtime

Profile



&#x20;       │



&#x20;       ▼



Context Collector



&#x20;       │



&#x20;       ▼



Context Merger



&#x20;       │



&#x20;       ▼



Prioritizer



&#x20;       │



&#x20;       ▼



Snapshot

```



\---



\# Decision Data Flow



```text

Reasoning



&#x20;     │



&#x20;     ▼



Decision Generator



&#x20;     │



&#x20;     ▼



Evaluation



&#x20;     │



&#x20;     ▼



Approval



&#x20;     │



&#x20;     ▼



Execution Plan

```



\---



\# Learning Cycle



```text

Execution



&#x20;     │



&#x20;     ▼



Validation



&#x20;     │



&#x20;     ▼



Reflection



&#x20;     │



&#x20;     ▼



Learning



&#x20;     │



&#x20;     ▼



Brain Evolution



&#x20;     │



&#x20;     ▼



Next Execution

```



\---



\# Mandatory Rules



Every execution must follow exactly this order:



1\. Task Intake



2\. Goal



3\. Context



4\. Memory



5\. Eye



6\. Reasoning



7\. Decision



8\. Planning



9\. Agent Orchestration



10\. Runtime



11\. Communication



12\. Validation



13\. Reflection



14\. Learning



15\. Brain Evolution



16\. Completion



No stage may be skipped.



No module may reorder these stages.



This execution flow is frozen for Platform v1.0.

