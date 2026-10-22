"""Pattern 7: Tiered Agent Memory (Sensory, Working Context & Persistent Disk Storage)."""
import os
import json
import time
from typing import Dict, Any, List

class TieredMemory:
    def __init__(self, storage_file: str = "/tmp/agent_memory.json"):
        self.storage_file = storage_file
        self.working_buffer: List[Dict[str, Any]] = []
        self.persistent_store: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def commit(self, key: str, value: Any):
        self.persistent_store[key] = {"value": value, "updated_at": time.time()}
        with open(self.storage_file, "w") as f:
            json.dump(self.persistent_store, f, indent=2)

    def append_buffer(self, role: str, content: str):
        self.working_buffer.append({"role": role, "content": content, "timestamp": time.time()})

    def recall(self, key: str) -> Any:
        item = self.persistent_store.get(key)
        return item["value"] if item else None
