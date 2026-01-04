from dotenv import load_dotenv
load_dotenv()   # MUST be first

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.query import router as query_router

# Import the API routes
from api.v1.query import router as query_router

# Load environment variables
load_dotenv()

# Initialize the FastAPI app
app = FastAPI(
    title="Book-Side RAG Chatbot API",
    description="API for the RAG chatbot integrated with the Physical AI & Humanoid Robotics book",
    version="1.0.0"
)

# Add CORS middleware for Docusaurus integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Docusaurus site URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(query_router)

@app.get("/")
def read_root():
    return {"message": "Book-Side RAG Chatbot API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)