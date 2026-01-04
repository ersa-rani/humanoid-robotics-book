from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class SourceCitation(BaseModel):
    title: str
    url: str


class QueryRequest(BaseModel):
    id: Optional[str] = None
    content: str
    timestamp: Optional[datetime] = None
    userId: Optional[str] = None
    selectedText: Optional[str] = None
    sessionId: Optional[str] = None


class ChatResponse(BaseModel):
    id: str
    content: str
    timestamp: datetime
    queryId: str
    sourceBookContentIds: List[str]
    confidence: float
    citations: List[SourceCitation]
