
from pydantic import BaseModel
from typing import Dict, Any

class AgentMessage(BaseModel):
    sender: str
    receiver: str
    task: str
    payload: Dict[str, Any]
