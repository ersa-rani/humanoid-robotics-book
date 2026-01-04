from datetime import datetime
import logging
from models.query import QueryRequest, ChatResponse, SourceCitation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockRAGService:
    def __init__(self):
        logger.info("Mock RAG Service initialized (for development without API quota)")

    async def query_full_book(self, query_request: QueryRequest) -> ChatResponse:
        try:
            logger.info(f"Mock query received: {query_request.content}")
            
            # Simple mock responses for common queries
            content_lower = query_request.content.lower()
            if "chapter" in content_lower or "chapters" in content_lower:
                answer = "The book contains 12 chapters covering various aspects of humanoid robotics."
            elif "author" in content_lower or "who wrote" in content_lower:
                answer = "The book is authored by experts in the field of humanoid robotics."
            elif "topic" in content_lower or "subject" in content_lower:
                answer = "This book covers topics including locomotion, control systems, perception, and human-robot interaction in humanoid robotics."
            else:
                answer = f"This is a mock response for your query: '{query_request.content}'. In production, this would be answered by an AI model connected to the book's content."
            
            return ChatResponse(
                id=f"mock_resp_{int(datetime.now().timestamp())}",
                content=answer,
                timestamp=datetime.now(),
                queryId=query_request.id or "auto",
                sourceBookContentIds=[],
                confidence=0.8,
                citations=[]
            )

        except Exception as e:
            logger.exception("Mock RAG query failed")
            raise RuntimeError(str(e))