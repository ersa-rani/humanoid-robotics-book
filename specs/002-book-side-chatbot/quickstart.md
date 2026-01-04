# Quickstart: Book-Side RAG Chatbot

## Overview
This guide will help you get the Book-Side RAG Chatbot up and running in your development environment.

## Prerequisites
- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for FastAPI backend)
- Yarn or npm (for frontend dependencies)
- pip (for Python dependencies)
- Qdrant running locally or accessible remotely

## Setup Instructions

### 1. Clone and Navigate to Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup (FastAPI)
```bash
# Navigate to backend directory (or root if monorepo)
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY=your_openai_api_key
export QDRANT_URL=your_qdrant_url
export QDRANT_API_KEY=your_qdrant_api_key  # if required
```

### 3. Frontend Setup (Docusaurus)
```bash
# Navigate to project root
cd ..

# Install dependencies
yarn install
# or npm install

# Build the site
yarn build
# or npm run build
```

### 4. Running the Application

#### Backend (FastAPI)
```bash
# From the backend directory
cd backend
source venv/bin/activate  # Activate virtual environment
uvicorn main:app --reload --port 8000
```

#### Frontend (Docusaurus)
```bash
# From the project root
yarn start
# or npm start
```

### 5. Indexing Book Content for RAG
Before the chatbot can answer questions, you need to index your book content into Qdrant:

```bash
# From the backend directory
cd backend
source venv/bin/activate
python -m scripts.index_book_content --source-path /path/to/book/content
```

## Configuration
- The chatbot is automatically injected into all documentation pages via the Docusaurus theme override at `src/theme/DocItem/Layout.tsx`
- API endpoints are configured to connect to the backend service
- Styling adapts to the current light/dark theme of the book interface

## Testing the Integration
1. Navigate to any documentation page
2. Verify that the chatbot panel appears on the right side
3. Try asking a question about the book content
4. Test the text selection feature by highlighting text and asking a question about it