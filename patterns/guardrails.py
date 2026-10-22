"""Pattern 8: Schema Enforcer, Semantic Boundary & Anti-Hallucination Guardrails."""
import re
import json
from typing import Dict, Any, Tuple

class GuardrailEngine:
    def __init__(self, allowed_keys: List[str] = None, banned_patterns: List[str] = None):
        self.allowed_keys = allowed_keys or []
        self.banned_patterns = banned_patterns or []

    def validate_json_contract(self, text: str) -> Tuple[bool, Any]:
        try:
            m = re.search(r"\{.*\}", text, re.DOTALL)
            if not m:
                return False, "No JSON found in text."
            parsed = json.loads(m.group(0))
            if self.allowed_keys:
                missing = [k for k in self.allowed_keys if k not in parsed]
                if missing:
                    return False, f"Missing required contract keys: {missing}"
            return True, parsed
        except Exception as e:
            return False, f"JSON parse error: {e}"

    def check_banned_content(self, text: str) -> Tuple[bool, str]:
        for pat in self.banned_patterns:
            if re.search(pat, text, re.IGNORECASE):
                return False, f"Triggered banned guardrail pattern: '{pat}'"
        return True, "Safe."
