from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    """
    Model for individual chat messages
    """
    id: str
    content: str
    role: str  # 'user' or 'assistant'
    timestamp: datetime
    userId: Optional[str] = None
    sessionId: Optional[str] = None

class ChatSession(BaseModel):
    """
    Model for chat sessions
    """
    id: str
    userId: Optional[str] = None
    messages: List[ChatMessage]
    createdAt: datetime
    updatedAt: datetime