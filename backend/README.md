# Book-Side RAG Chatbot Backend

This is the backend service for the Book-Side RAG Chatbot, built with FastAPI. It provides APIs for querying the book content using RAG (Retrieval-Augmented Generation).

## Prerequisites

- Python 3.11+
- pip

## Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env to add your API keys
   ```

## Running the Service

To run the service in development mode:
```bash
cd backend
source   # Activate virtual environment
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

## venv/bin/activateAPI Endpoints

- `GET /` - Root endpoint
- `POST /v1/query` - Query the full book content
- `POST /v1/query-selected` - Query with selected text as context
- `GET /health` - Health check endpoint

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key
- `QDRANT_URL` - URL for your Qdrant instance
- `QDRANT_API_KEY` - API key for Qdrant (if required)
- `ENVIRONMENT` - Environment name (development, production)
- `LOG_LEVEL` - Logging level (info, debug, warning, error)