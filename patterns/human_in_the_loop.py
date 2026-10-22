"""Pattern 9: State Suspension, Approval Gates & Human-in-the-Loop Semantics."""
from typing import Dict, Any, Callable

class HumanInTheLoopGate:
    def __init__(self, risk_threshold: float = 0.7):
        self.risk_threshold = risk_threshold
        self.pending_actions: Dict[str, Dict[str, Any]] = {}

    def assess_and_dispatch(self, action_id: str, tool_name: str, params: Dict[str, Any], risk_score: float, executor: Callable) -> Dict[str, Any]:
        if risk_score >= self.risk_threshold:
            self.pending_actions[action_id] = {"tool": tool_name, "params": params, "status": "WAITING_APPROVAL", "executor": executor}
            return {"status": "SUSPENDED", "action_id": action_id, "message": f"Action '{tool_name}' held for human approval (Risk: {risk_score})."}
        
        # Safe to run directly
        res = executor(**params)
        return {"status": "EXECUTED", "result": res}

    def approve(self, action_id: str) -> Dict[str, Any]:
        act = self.pending_actions.get(action_id)
        if not act:
            return {"status": "ERROR", "message": "Action not found."}
        res = act["executor"](**act["params"])
        act["status"] = "APPROVED_AND_EXECUTED"
        return {"status": "APPROVED", "result": res}
