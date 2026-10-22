"""Pattern 2: Plan-and-Solve (Two-Stage Strategic Planner & Tactical Executor)."""
import time
from typing import List, Dict, Any, Callable

class PlanAndSolveEngine:
    def __init__(self, planner: Callable[[str], List[str]], executor: Callable[[str], str]):
        self.planner = planner
        self.executor = executor

    def run(self, goal: str) -> Dict[str, Any]:
        start = time.time()
        plan = self.planner(goal)
        results = []
        for idx, step in enumerate(plan, 1):
            out = self.executor(step)
            results.append({"step_index": idx, "task": step, "output": out})
        
        return {
            "goal": goal,
            "plan_length": len(plan),
            "execution_trace": results,
            "duration_ms": round((time.time() - start) * 1000, 2)
        }
