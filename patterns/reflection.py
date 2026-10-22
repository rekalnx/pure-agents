"""Pattern 3: Reflection / Self-Critique (Actor-Critic Recursive Hardening)."""
from typing import Dict, Any, Callable

class ReflectionEngine:
    def __init__(self, generator: Callable[[str], str], critic: Callable[[str, str], Dict[str, Any]], max_rounds: int = 3):
        self.generator = generator
        self.critic = critic
        self.max_rounds = max_rounds

    def refine(self, task: str) -> Dict[str, Any]:
        draft = self.generator(task)
        history = []
        for r in range(self.max_rounds):
            eval_res = self.critic(task, draft)
            passed = eval_res.get("passed", False)
            feedback = eval_res.get("feedback", "No feedback.")
            history.append({"round": r + 1, "draft": draft, "critique": feedback, "passed": passed})
            if passed:
                return {"final_artifact": draft, "rounds_taken": len(history), "audit_history": history}
            draft = self.generator(f"Task: {task}\nPrevious Draft: {draft}\nCritique to Fix: {feedback}")

        return {"final_artifact": draft, "rounds_taken": len(history), "audit_history": history}
