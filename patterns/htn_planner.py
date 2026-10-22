"""Pattern 6: Hierarchical Task Network (HTN) Recursive Decomposition."""
from typing import List, Dict, Any

class HTNPlanner:
    def __init__(self):
        self.methods: Dict[str, List[str]] = {}

    def add_decomposition(self, compound_task: str, subtasks: List[str]):
        self.methods[compound_task] = subtasks

    def decompose(self, task: str) -> List[str]:
        if task not in self.methods:
            return [task] # Primitive action
        plan = []
        for sub in self.methods[task]:
            plan.extend(self.decompose(sub))
        return plan
