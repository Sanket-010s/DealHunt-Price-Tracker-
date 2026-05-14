from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAlerter(ABC):
    @abstractmethod
    async def send_alert(self, message: str, metadata: Dict[str, Any] = None) -> bool:
        """Send alert notification"""
        pass
