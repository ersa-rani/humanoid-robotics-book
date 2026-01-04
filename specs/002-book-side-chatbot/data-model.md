# Data Model: Book-Side RAG Chatbot

## Entities

### Book Content
- **Description**: The textual and media content of the Physical AI & Humanoid Robotics book that serves as the knowledge base for the chatbot
- **Fields**: 
  - id: string (unique identifier for book content section)
  - title: string (title of the section/chapter)
  - content: string (the actual text content)
  - metadata: object (additional information like author, date, etc.)
  - embedding: float[] (vector representation for RAG search)
- **Relationships**: Contains many Chat Responses (as context for answers)
- **Validation**: Content must be non-empty, embedding must be properly formatted vector

### User Query
- **Description**: The text input from users asking questions about the book content
- **Fields**:
  - id: string (unique identifier for the query)
  - content: string (the actual question text)
  - timestamp: datetime (when the query was submitted)
  - userId: string (identifier for the user, if available)
  - selectedText: string (optional text selected by user to provide context)
  - sessionId: string (to group related queries)
- **Relationships**: Links to Book Content (for context) and generates Chat Response
- **Validation**: Content must be non-empty and under maximum length limit

### Chat Response
- **Description**: The AI-generated response to user queries, based on the book content
- **Fields**:
  - id: string (unique identifier for the response)
  - content: string (the actual response text)
  - timestamp: datetime (when the response was generated)
  - queryId: string (reference to the original query)
  - sourceBookContentIds: string[] (IDs of book content used to generate response)
  - confidence: float (confidence score of the response)
  - citations: object[] (references to specific parts of book content)
- **Relationships**: Belongs to User Query and is derived from Book Content
- **Validation**: Content must be non-empty, confidence must be between 0 and 1

### Selected Text
- **Description**: Portion of book content highlighted by the user to provide context for their question
- **Fields**:
  - id: string (unique identifier for the selection)
  - content: string (the actual selected text)
  - bookContentId: string (reference to the book content where selection was made)
  - startOffset: number (character position where selection starts)
  - endOffset: number (character position where selection ends)
  - context: string (surrounding text for context)
- **Relationships**: Links to Book Content and is part of User Query
- **Validation**: Content must be non-empty and under maximum length limit

## State Transitions

### Query Processing Flow
1. User Query is created when user submits a question
2. System processes the query against Book Content using RAG
3. Chat Response is generated and associated with the original query
4. Response is sent back to the user interface

### Text Selection Flow
1. User selects text in Book Content
2. Selected Text entity is created with position and content details
3. When user submits query, Selected Text is included as context
4. System uses both query and selected text to generate more contextual response