# pure-agents 🧠

> **The Definitive, Zero-Framework Guide to Autonomous AI Agent Architectures in Pure Python Standard Library.**
> **Zero Pip Installs. No LangChain. No CrewAI. No Bloatware. Just First Principles.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![Tests: 10/10 Passing](https://img.shields.io/badge/tests-10%2F10%20passing-success.svg)](tests/)
[![Dependencies: ZERO](https://img.shields.io/badge/dependencies-ZERO-orange.svg)]()

Modern agentic frameworks like LangChain, CrewAI, and AutoGen suffer from immense architectural bloat: hundreds of nested classes, obscure abstractions, brittle dependencies, and high execution latency.

`pure-agents` demonstrates that **every fundamental agentic architecture** can be implemented cleanly using only the **Python standard library**.

---

## ⚡ Performance: Why Pure Stdlib?

Benchmark run on Linux x86_64:

| Operation | pure-agents (Stdlib) | Typical Heavy Framework | Speedup |
|---|---|---|---|
| **Tool Dispatch** | **0.95 µs** | ~2.5 ms | **~2,600x faster** |
| **HTN Decomposition** | **0.39 µs** | ~1.8 ms | **~4,500x faster** |
| **In-Memory Example Routing** | **0.06 ms** | ~45 ms (vector DB client) | **~750x faster** |
| **Memory Footprint** | **~12 MB** | 250 MB – 600 MB | **95% lighter** |

---

## 🏗️ 10 Production-Grade Architectures

Every architecture is fully modularized with dedicated implementations and test suites:

| # | Architecture | Module | Description |
|---|---|---|---|
| 1 | **ReAct** | [`patterns/react.py`](patterns/react.py) | Thought $\to$ Action $\to$ Observation cyclic execution engine |
| 2 | **Plan-and-Solve** | [`patterns/plan_solve.py`](patterns/plan_solve.py) | Strategic two-stage task decomposition & tactical worker pipeline |
| 3 | **Reflection** | [`patterns/reflection.py`](patterns/reflection.py) | Actor-Critic self-critique loop that recursively hardens artifacts |
| 4 | **Tool Dispatcher** | [`patterns/tool_dispatcher.py`](patterns/tool_dispatcher.py) | Schema-validated function registry using native `inspect` |
| 5 | **Blackboard Swarm** | [`patterns/blackboard_swarm.py`](patterns/blackboard_swarm.py) | Decoupled multi-agent coordination via shared memory bus |
| 6 | **HTN Planner** | [`patterns/htn_planner.py`](patterns/htn_planner.py) | Hierarchical Task Network recursive goal decomposition |
| 7 | **Tiered Memory** | [`patterns/memory_state.py`](patterns/memory_state.py) | Working memory buffer + persistent disk storage state machine |
| 8 | **Guardrail Engine** | [`patterns/guardrails.py`](patterns/guardrails.py) | Output containment, JSON contract validator & anti-hallucination gates |
| 9 | **Human-in-the-Loop** | [`patterns/human_in_the_loop.py`](patterns/human_in_the_loop.py) | State suspension, approval gates & risk-based interruption |
| 10 | **Few-Shot Router** | [`patterns/few_shot_router.py`](patterns/few_shot_router.py) | In-memory semantic example selector without external vector DBs |

---

## 📂 Repository Structure

```text
pure-agents/
├── pure_agents.py              # Single-file runnable showcase of all patterns
├── patterns/                   # Modularized production implementations
│   ├── react.py
│   ├── plan_solve.py
│   ├── reflection.py
│   ├── tool_dispatcher.py
│   ├── blackboard_swarm.py
│   ├── htn_planner.py
│   ├── memory_state.py
│   ├── guardrails.py
│   ├── human_in_the_loop.py
│   └── few_shot_router.py
├── tests/                      # Full unit test suite (100% passing)
│   └── test_all_patterns.py
├── benchmarks/                 # Latency & throughput micro-benchmarks
│   └── benchmark_latency.py
└── examples/                   # Real-world agent pipelines
    └── research_assistant.py
```

---

## 🏃 Quickstart

Clone and run the complete test suite instantly:

```bash
git clone https://github.com/rekalnx/pure-agents.git
cd pure-agents
python3 -m unittest tests/test_all_patterns.py
```

Run benchmarks:
```bash
python3 benchmarks/benchmark_latency.py
```

---

## 📄 License
MIT © [Reihan Valentino (rekalnx)](https://github.com/rekalnx)
