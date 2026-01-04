<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0 (MINOR: New principle/section added)
- Modified principles: Added 6 new principles for Book-Integrated Chatbot
- Added sections: Implementation Constraints, Quality Assurance
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/*.md ⚠ pending
- Follow-up TODOs: RATIFICATION_DATE needs to be set to actual date of original adoption
-->
# Book-Integrated Chatbot Constitution

## Core Principles

### I. UI-First Integration
The chatbot MUST be visible inside the book UI at all times; it cannot be hidden, optional, or external. This ensures seamless user experience while reading documentation.

### II. Mandatory Placement
Chatbot must appear either beside the book content (right sidebar) or below the book content (bottom dock), must scroll with the book or remain sticky, and must be visible on every documentation page.

### III. Forbidden Implementation Patterns
No external chatbot page, no separate route (/chat), no iframe embeds, no hidden floating-only button. These patterns violate the core requirement of integrated experience.

### IV. Interactive Functionality
Users can read and chat simultaneously, users can select book text and ask questions, chatbot must clearly indicate whether it's answering from full book or selected text.

### V. Technology Stack Compliance
Frontend: Docusaurus (React), Backend: FastAPI, RAG: Qdrant + OpenAI Agents, UI must be implemented inside Docusaurus layout. Deviation from this stack requires explicit architectural approval.

### VI. Success Validation
If the chatbot is not visible while reading the book, the feature is considered FAILED. This is the primary acceptance criterion.

## Implementation Constraints

The following technology stack is mandated for this project:
- Frontend: Docusaurus (React)
- Backend: FastAPI
- RAG: Qdrant + OpenAI Agents
- UI must be implemented inside Docusaurus layout

All implementations must comply with these technology choices unless explicitly approved otherwise through architectural decision records.

## Quality Assurance

All features must undergo validation to ensure:
- Chatbot visibility during book reading
- Proper interaction between book content and chatbot
- Correct indication of information source (full book vs. selected text)
- Compliance with forbidden pattern restrictions

## Governance

This constitution supersedes all other development practices for the Book-Integrated Chatbot project. Amendments require documentation in the form of Architectural Decision Records (ADRs) with proper approval and migration planning.

All pull requests and code reviews must verify compliance with these principles. Complexity must be justified with clear benefits to the core user experience.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE): Date of original adoption | **Last Amended**: 2025-12-30
