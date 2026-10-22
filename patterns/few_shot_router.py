"""Pattern 10: Dynamic Few-Shot In-Memory Example Router without External Vector DBs."""
import math
import re
from typing import List, Dict, Any

class InMemoryExampleRouter:
    def __init__(self):
        self.examples: List[Dict[str, str]] = []

    def add_example(self, query: str, response: str):
        self.examples.append({"query": query, "response": response})

    def _cosine_sim(self, words1: List[str], words2: List[str]) -> float:
        set1, set2 = set(words1), set(words2)
        intersection = set1.intersection(set2)
        if not intersection: return 0.0
        return len(intersection) / math.sqrt(len(set1) * len(set2))

    def route_top_k(self, current_query: str, k: int = 2) -> List[Dict[str, str]]:
        q_tokens = re.findall(r"\w+", current_query.lower())
        scored = []
        for ex in self.examples:
            ex_tokens = re.findall(r"\w+", ex["query"].lower())
            score = self._cosine_sim(q_tokens, ex_tokens)
            scored.append((score, ex))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:k]]
