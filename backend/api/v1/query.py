from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import logging

from models.query import QueryRequest, ChatResponse
from services.rag_service import RAGService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create API router
router = APIRouter(prefix="/v1", tags=["query"])

# Initialize RAG service
rag_service = RAGService()

class QuerySelectedRequest(BaseModel):
    query: QueryRequest
    selectedText: str

@router.post("/query", response_model=ChatResponse)
async def query_full_book_endpoint(request: QueryRequest):
    """
    Submit a question about the book content and receive a response based on the full book
    """
    try:
        logger.info(f"Received query: {request.content}")
        response = await rag_service.query_full_book(request)
        return response
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
