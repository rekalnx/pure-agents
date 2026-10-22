"""Comprehensive Test Suite for pure-agents."""
import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from patterns.react import ReActEngine
from patterns.plan_solve import PlanAndSolveEngine
from patterns.reflection import ReflectionEngine
from patterns.tool_dispatcher import ToolRegistry
from patterns.blackboard_swarm import BlackboardSwarm
from patterns.htn_planner import HTNPlanner
from patterns.memory_state import TieredMemory
from patterns.guardrails import GuardrailEngine
from patterns.human_in_the_loop import HumanInTheLoopGate
from patterns.few_shot_router import InMemoryExampleRouter

class TestPureAgents(unittest.TestCase):
    def test_react(self):
        engine = ReActEngine({"calc": lambda x: eval(x)})
        ans = engine.execute("Calculate 2+2", lambda p: "Thought: Calculate\nAction: calc[2+2]\n" if "Observation:" not in p else "Final Answer: 4")
        self.assertEqual(ans, "4")

    def test_plan_solve(self):
        engine = PlanAndSolveEngine(lambda g: ["a", "b"], lambda s: f"done_{s}")
        res = engine.run("test goal")
        self.assertEqual(res["plan_length"], 2)

    def test_reflection(self):
        def mock_gen(prompt):
            if "Critique" in prompt: return "secure code"
            return "insecure code"
        def mock_critic(t, draft):
            return {"passed": True if draft == "secure code" else False, "feedback": "Add security"}
        engine = ReflectionEngine(mock_gen, mock_critic)
        res = engine.refine("Write code")
        self.assertEqual(res["final_artifact"], "secure code")

    def test_tool_dispatcher(self):
        reg = ToolRegistry()
        @reg.register("add", "adds two numbers")
        def add(a: int, b: int) -> int: return a + b
        res = reg.dispatch("add", '{"a": 5, "b": 7}')
        self.assertEqual(res, 12)

    def test_blackboard_swarm(self):
        bb = BlackboardSwarm()
        bb.broadcast("worker-1", "result", 100)
        self.assertEqual(bb.query_topic("result"), 100)

    def test_htn(self):
        htn = HTNPlanner()
        htn.add_decomposition("cook", ["prep", "fry"])
        self.assertEqual(htn.decompose("cook"), ["prep", "fry"])

    def test_memory(self):
        mem = TieredMemory("/tmp/test_mem.json")
        mem.commit("user", "Reihan")
        self.assertEqual(mem.recall("user"), "Reihan")

    def test_guardrails(self):
        gr = GuardrailEngine(allowed_keys=["name", "role"])
        valid, _ = gr.validate_json_contract('{"name": "Luci", "role": "Commander"}')
        self.assertTrue(valid)

    def test_hitl(self):
        gate = HumanInTheLoopGate(0.5)
        res = gate.assess_and_dispatch("1", "delete_db", {}, 0.9, lambda: "deleted")
        self.assertEqual(res["status"], "SUSPENDED")
        app = gate.approve("1")
        self.assertEqual(app["status"], "APPROVED")

    def test_router(self):
        router = InMemoryExampleRouter()
        router.add_example("how to code in python", "python is great")
        router.add_example("recipe for cake", "bake at 180C")
        top = router.route_top_k("writing python software", k=1)
        self.assertEqual(top[0]["query"], "how to code in python")

if __name__ == "__main__":
    unittest.main()
