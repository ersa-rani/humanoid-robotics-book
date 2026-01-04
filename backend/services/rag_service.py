from datetime import datetime
import logging
import os
from openai import OpenAI
from models.query import QueryRequest, ChatResponse, SourceCitation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)

class RAGService:
    def __init__(self):
        self.use_mock = os.getenv("USE_MOCK_SERVICE", "").lower() == "true"
        if self.use_mock:
            from .mock_rag_service import MockRAGService
            self.mock_service = MockRAGService()
            logger.info("RAG Service initialized with mock service (for development)")
        else:
            self.client = get_openai_client()
            logger.info("RAG Service initialized (basic real-time mode)")

    async def query_full_book(self, query_request: QueryRequest) -> ChatResponse:
        try:
            logger.info(f"Query received: {query_request.content}")

            if self.use_mock:
                return await self.mock_service.query_full_book(query_request)

            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Answer simply using general book knowledge."},
                    {"role": "user", "content": query_request.content}
                ]
            )

            answer = completion.choices[0].message.content

            return ChatResponse(
                id=f"resp_{int(datetime.now().timestamp())}",
                content=answer,
                timestamp=datetime.now(),
                queryId=query_request.id or "auto",
                sourceBookContentIds=[],
                confidence=0.6,
                citations=[]
            )

        except Exception as e:
            logger.exception("RAG query failed")
            raise RuntimeError(str(e))
