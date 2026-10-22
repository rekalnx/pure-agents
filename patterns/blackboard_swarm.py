"""Pattern 5: Shared-Memory Blackboard Multi-Agent Swarm Orchestrator."""
import time
from typing import Dict, Any, List

class BlackboardSwarm:
    def __init__(self):
        self.state: Dict[str, Any] = {}
        self.events: List[Dict[str, Any]] = []

    def broadcast(self, agent_id: str, topic: str, payload: Any):
        ev = {"agent_id": agent_id, "topic": topic, "payload": payload, "timestamp": time.time()}
        self.events.append(ev)
        self.state[topic] = payload

    def query_topic(self, topic: str) -> Any:
        return self.state.get(topic)

    def get_agent_activity(self, agent_id: str) -> List[Dict[str, Any]]:
        return [e for e in self.events if e["agent_id"] == agent_id]
