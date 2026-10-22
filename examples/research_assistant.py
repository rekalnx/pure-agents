"""End-to-End Example: Autonomous Research & Code Verification Assistant."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from patterns.react import ReActEngine
from patterns.plan_solve import PlanAndSolveEngine
from patterns.guardrails import GuardrailEngine
from patterns.tool_dispatcher import ToolRegistry

def main():
    print("=== Demo: Autonomous Research Pipeline ===")
    
    # 1. Setup Tool Registry
    registry = ToolRegistry()
    @registry.register("calculator", "evaluates math formulas")
    def calc(expr: str) -> str:
        return str(eval(expr))

    @registry.register("lookup_db", "queries internal knowledge")
    def lookup(query: str) -> str:
        kb = {"speed_of_light": "299,792,458 m/s", "planck": "6.626e-34 J*s"}
        return kb.get(query, "Key not found")

    print("[+] Tools registered:", list(registry.tools.keys()))

    # 2. Strategic Planner
    planner = PlanAndSolveEngine(
        planner=lambda g: [f"Identify constants for {g}", f"Compute energy density", f"Format response"],
        executor=lambda task: f"Completed: {task}"
    )
    plan_res = planner.run("Calculate photon energy")
    print(f"[+] Execution Plan: {plan_res['plan_length']} phases completed.")

    # 3. Guardrail Output Audit
    guardrail = GuardrailEngine(banned_patterns=[r"password", r"secret_key", r"eval\(.*input"])
    safe, msg = guardrail.check_banned_content("Here is the photon formula calculation.")
    print(f"[+] Guardrail Safety Gate: {msg}")

if __name__ == "__main__":
    main()
