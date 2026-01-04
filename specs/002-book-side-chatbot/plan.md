# Implementation Plan: Book-Side RAG Chatbot

**Branch**: `002-book-side-chatbot` | **Date**: 2025-12-30 | **Spec**: [specs/002-book-side-chatbot/spec.md](specs/002-book-side-chatbot/spec.md)
**Input**: Feature specification from `/specs/002-book-side-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a RAG chatbot integrated directly into the Physical AI & Humanoid Robotics book interface. The chatbot will appear as a right-side panel beside book content, automatically visible on page load. The solution uses Docusaurus for the frontend, FastAPI for the backend, and Qdrant for RAG functionality. Users can ask questions about the book content and select/highlight text to send as context with their queries.

## Technical Context

**Language/Version**: TypeScript 5.0+ (for frontend), Python 3.11+ (for backend)
**Primary Dependencies**: Docusaurus (React-based), FastAPI, Qdrant, OpenAI Agents
**Storage**: Qdrant vector database for RAG, book content in Docusaurus
**Testing**: Jest/React Testing Library (frontend), pytest (backend)
**Target Platform**: Web (Docusaurus-based documentation site)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: <5 second response time for queries, <200ms UI interactions
**Constraints**: Must integrate directly with Docusaurus layout, no external pages, responsive design
**Scale/Scope**: Single documentation site with integrated chatbot functionality

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Design Compliance Verification

**I. UI-First Integration**: ✅
- Plan ensures chatbot visible inside book UI at all times via Docusaurus Layout override

**II. Mandatory Placement**: ✅
- Plan implements right-side panel beside book content as required

**III. Forbidden Implementation Patterns**: ✅
- Plan avoids external chatbot page, separate routes, iframes, and hidden buttons
- Chatbot integrated directly in Docusaurus layout

**IV. Interactive Functionality**: ✅
- Plan includes simultaneous reading/chatting and text selection capabilities

**V. Technology Stack Compliance**: ✅
- Frontend: Docusaurus (React) - confirmed in plan
- Backend: FastAPI - confirmed in plan
- RAG: Qdrant + OpenAI Agents - confirmed in plan
- UI implemented inside Docusaurus layout - confirmed in plan

**VI. Success Validation**: ✅
- Plan ensures chatbot is visible while reading book content

### Post-Design Compliance Verification

**I. UI-First Integration**: ✅
- Confirmed in data model and API contracts: chatbot integrated directly in UI

**II. Mandatory Placement**: ✅
- Confirmed in frontend structure: right-side panel implementation planned

**III. Forbidden Implementation Patterns**: ✅
- Confirmed in API design: no external pages or separate routes created

**IV. Interactive Functionality**: ✅
- Confirmed in data model: Selected Text entity supports text selection feature

**V. Technology Stack Compliance**: ✅
- Confirmed in backend structure: FastAPI with Qdrant and OpenAI integration

**VI. Success Validation**: ✅
- Confirmed through implementation approach: chatbot visibility guaranteed by Docusaurus theme override

## Project Structure

### Documentation (this feature)

```text
specs/002-book-side-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Web application (frontend + backend)
src/
├── components/
│   └── BookChatbot/
│       ├─ BookChatbot.tsx
│       ├─ ChatWindow.tsx
│       ├─ ChatInput.tsx
│       └─ useSelection.ts
└── theme/
    └── DocItem/
        └─ Layout.tsx   # chatbot injected here

backend/
├── main.py              # FastAPI application entrypoint
├── models/
│   ├── query.py         # Query request/response models
│   └── chat.py          # Chat-related models
├── services/
│   ├── rag_service.py   # RAG service for book content
│   └── chat_service.py  # Chat service
├── api/
│   └── v1/
│       ├── chat.py      # Chat endpoints
│       └── query.py     # Query endpoints
└── tests/
    ├── unit/
    └── integration/

contracts/
└── openapi.yaml         # API contract for chatbot endpoints

# Docusaurus configuration files
docusaurus.config.js
sidebars.js
```

**Structure Decision**: Web application structure selected to separate frontend (Docusaurus) and backend (FastAPI) concerns while maintaining integration through the Docusaurus theme override.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
