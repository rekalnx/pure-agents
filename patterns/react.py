"""Pattern 1: ReAct (Reasoning and Acting) - Pure Python Stdlib Implementation."""
import re
from typing import Dict, Callable, List, Tuple

class ReActEngine:
    def __init__(self, tools: Dict[str, Callable[[str], str]], max_iterations: int = 6):
        self.tools = tools
        self.max_iterations = max_iterations
        self.trace: List[Dict[str, str]] = []

    def execute(self, question: str, llm_simulator: Callable[[str], str]) -> str:
        prompt = f"Question: {question}\nSolve using Thought -> Action -> Observation cycle."
        for step in range(self.max_iterations):
            response = llm_simulator(prompt)
            thought_match = re.search(r"Thought:\s*(.*?)(?=\nAction:|$)", response, re.DOTALL)
            action_match = re.search(r"Action:\s*([a-zA-Z0-9_]+)\[(.*?)\]", response)
            
            thought = thought_match.group(1).strip() if thought_match else "Analyzing next step."
            
            if not action_match:
                if "Final Answer:" in response:
                    final_ans = response.split("Final Answer:")[-1].strip()
                    self.trace.append({"step": step+1, "thought": thought, "final": final_ans})
                    return final_ans
                return response.strip()

            tool_name = action_match.group(1)
            tool_input = action_match.group(2)
            
            tool_fn = self.tools.get(tool_name, lambda x: f"Error: Tool '{tool_name}' not found.")
            observation = str(tool_fn(tool_input))
            
            self.trace.append({
                "step": step+1,
                "thought": thought,
                "action": f"{tool_name}[{tool_input}]",
                "observation": observation
            })
            prompt += f"\nThought: {thought}\nAction: {tool_name}[{tool_input}]\nObservation: {observation}\n"

        return "Error: Maximum execution iterations exceeded without resolution."
