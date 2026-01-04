---
id: 1
title: Book-Integrated Chatbot Constitution Update
stage: constitution
date: 2025-12-30
surface: agent
model: Qwen
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, chatbot, ui]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution # Project Constitution — Book-Integrated Chatbot (UI Mandatory)

## Primary Rule (Non-Negotiable)
The chatbot MUST be visible inside the book UI.
It cannot be hidden, optional, or external.

## UI Placement Rules
- Chatbot must appear:
  - Either BESIDE the book content (right sidebar)
  - OR BELOW the book content (bottom dock)
- Chatbot must scroll with the book or remain sticky
- Chatbot must be visible on every documentation page

## Forbidden Patterns
- ❌ No external chatbot page
- ❌ No separate route (/chat)
- ❌ No iframe embeds
- ❌ No hidden floating-only button

## Interaction Rules
- Users can read and chat simultaneously
- Users can select book text and ask questions
- Chatbot must clearly indicate:
  - "Answering from full book"
  - "Answering from selected text"

## Technology Lock
- Frontend: Docusaurus (React)
- Backend: FastAPI
- RAG: Qdrant + OpenAI Agents
- UI must be implemented inside Docusaurus layout

## Success Condition
If the chatbot is not visible while reading the book, the feature is considered FAILED.
```

## Response snapshot

The constitution for the Book-Integrated Chatbot project has been successfully created with the following key elements:

1. **Core Principles** (6 total):
   - UI-First Integration: Chatbot must be visible inside the book UI at all times
   - Mandatory Placement: Chatbot must appear beside or below book content
   - Forbidden Implementation Patterns: No external pages, separate routes, iframes, or hidden buttons
   - Interactive Functionality: Users can read and chat simultaneously with text selection capability
   - Technology Stack Compliance: Docusaurus (React) frontend, FastAPI backend, Qdrant + OpenAI Agents for RAG
   - Success Validation: Feature fails if chatbot is not visible while reading

2. **Implementation Constraints**: Mandated technology stack with compliance requirements

3. **Quality Assurance**: Validation requirements for chatbot visibility and functionality

4. **Governance**: Amendment procedures and compliance expectations

Version updated to 1.1.0 with last amended date set to 2025-12-30.

## Outcome

- ✅ Impact: New constitution established for Book-Integrated Chatbot project
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with new constitution
- 🔁 Next prompts: /sp.specify to implement feature specification based on updated constitution
- 🧠 Reflection: Constitution properly reflects all requirements from user input with appropriate governance structure

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A