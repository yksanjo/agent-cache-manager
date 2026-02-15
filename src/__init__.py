"""Agent Cache Manager - Cache management for agents."""
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

class AgentCacheManager:
    def __init__(self, ttl: int = 300):
        self.cache: Dict[str, tuple] = {}
        self.ttl = ttl
    
    def set(self, key: str, value: Any) -> None:
        self.cache[key] = (value, datetime.now())
    
    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            val, ts = self.cache[key]
            if (datetime.now() - ts).seconds < self.ttl:
                return val
            del self.cache[key]
        return None

__all__ = ["AgentCacheManager"]
