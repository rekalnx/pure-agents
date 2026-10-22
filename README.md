# pure-agents 🧠

> **10 Essential Autonomous AI Agent Architectures implemented in Pure Python Standard Library.**
> **Zero Frameworks. Zero Pip Installs. No LangChain. No CrewAI. Just First Principles.**

Developers love understanding how systems work from the bare metal. Frameworks like LangChain, CrewAI, and AutoGen wrap simple concepts into thousands of lines of abstractions, making debugging and optimization impossible.

`pure-agents` demystifies agentic design patterns with clean, standalone, standard-library Python.

---

## 🏗️ 10 Architectures Included

1. **ReAct (Reasoning + Acting)**: The classic Thought $\to$ Action $\to$ Observation execution cycle.
2. **Plan-and-Solve**: Strategic two-stage planning with tactical worker execution.
3. **Reflection (Actor-Critic)**: Self-evaluating agents that critique and harden their own code/answers.
4. **Tool-Calling Dispatcher**: Schema-validated function registry and execution engine.
5. **Blackboard Multi-Agent Swarm**: Decoupled multi-agent orchestration via shared memory.
6. **Dynamic Few-Shot Selector**: Contextual in-memory example routing without external vector DBs.
7. **Hierarchical Task Network (HTN)**: Recursive goal decomposition into primitive actions.
8. **Memory State Machine**: Short-term buffer, working memory, and persistent disk-persisted recall.
9. **Guardrail Evaluator**: Output containment, regex boundary enforcement, and anti-hallucination gates.
10. **Human-in-the-Loop Interrupter**: State suspension and resume semantics for high-stakes tool execution.

---

## 🏃 Quickstart

Clone and run instantly without installing anything:

```bash
git clone https://github.com/rekalnx/pure-agents.git
cd pure-agents
python3 pure_agents.py
```

---

## 📄 License
MIT © [Reihan Valentino (rekalnx)](https://github.com/rekalnx)
