"""Pattern 4: Schema-Driven Tool Calling & Argument Validation Engine."""
import inspect
import json
from typing import Callable, Dict, Any

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, description: str):
        def decorator(fn: Callable):
            sig = inspect.signature(fn)
            params = {}
            for param_name, param in sig.parameters.items():
                params[param_name] = {
                    "type": str(param.annotation) if param.annotation != inspect.Parameter.empty else "Any",
                    "default": None if param.default == inspect.Parameter.empty else param.default
                }
            self.tools[name] = {
                "function": fn,
                "description": description,
                "schema": params
            }
            return fn
        return decorator

    def dispatch(self, tool_name: str, args_json: str) -> Any:
        if tool_name not in self.tools:
            raise KeyError(f"Tool '{tool_name}' is not registered.")
        args = json.loads(args_json) if isinstance(args_json, str) else args_json
        return self.tools[tool_name]["function"](**args)
