"""Benchmark: Execution overhead of pure stdlib patterns vs bloated frameworks."""
import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from patterns.tool_dispatcher import ToolRegistry
from patterns.htn_planner import HTNPlanner
from patterns.few_shot_router import InMemoryExampleRouter

def run_bench():
    print("=== Latency Benchmark: Pure Stdlib vs Framework Overhead ===")

    # Tool dispatch speed
    reg = ToolRegistry()
    @reg.register("bench_add", "add")
    def b_add(x: int) -> int: return x + 1

    t0 = time.perf_counter()
    for _ in range(10000):
        reg.dispatch("bench_add", '{"x": 10}')
    dispatch_time = (time.perf_counter() - t0) * 1000
    print(f"[*] 10,000 Tool Dispatches: {dispatch_time:.2f} ms ({dispatch_time/10000*1000:.3f} us/call)")

    # HTN Decomposition speed
    htn = HTNPlanner()
    htn.add_decomposition("root", ["task1", "task2"])
    htn.add_decomposition("task1", ["sub1", "sub2"])
    t0 = time.perf_counter()
    for _ in range(10000):
        htn.decompose("root")
    htn_time = (time.perf_counter() - t0) * 1000
    print(f"[*] 10,000 HTN Recursive Decompositions: {htn_time:.2f} ms ({htn_time/10000*1000:.3f} us/call)")

    # Example routing speed
    router = InMemoryExampleRouter()
    for i in range(50):
        router.add_example(f"query sample {i}", f"response {i}")
    t0 = time.perf_counter()
    for _ in range(1000):
        router.route_top_k("sample query test", k=3)
    router_time = (time.perf_counter() - t0) * 1000
    print(f"[*] 1,000 Semantic Example Routings: {router_time:.2f} ms ({router_time/1000:.3f} ms/query)")

if __name__ == "__main__":
    run_bench()
