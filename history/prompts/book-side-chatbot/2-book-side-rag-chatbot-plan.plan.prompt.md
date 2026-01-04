---
id: 2
title: Book-Side RAG Chatbot Plan
stage: plan
date: 2025-12-30
surface: agent
model: Qwen
feature: book-side-chatbot
branch: 002-book-side-chatbot
user: user
command: /sp.plan
labels: [planning, chatbot, ui, rag, docusaurus, fastapi]
links:
  spec: specs/002-book-side-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-book-side-chatbot/plan.md
 - specs/002-book-side-chatbot/research.md
 - specs/002-book-side-chatbot/data-model.md
 - specs/002-book-side-chatbot/contracts/openapi.yaml
 - specs/002-book-side-chatbot/quickstart.md
 - QWEN.md
tests:
 - none
---

## Prompt

```
/sp.plan # Technical Plan — Chatbot Beside / Below Book

## Frontend Architecture (MANDATORY)
Use Docusaurus `DocItem/Layout` or `Layout` override.

### Layout Strategy
- Wrap book content and chatbot in a CSS grid:
  - Left: Book Content
  - Right: Chatbot Panel
OR
- Render chatbot component at bottom of each doc page

## File Structure
src/
 ├─ components/
 │   └─ BookChatbot/
 │       ├─ BookChatbot.tsx
 │       ├─ ChatWindow.tsx
 │       ├─ ChatInput.tsx
 │       └─ useSelection.ts
 └─ theme/
     └─ DocItem/
         └─ Layout.tsx   ← chatbot injected here

## Rendering Logic
- Chatbot component auto-renders on every docs page
- No user action required to open chat
- Selection hook listens to highlighted book text

## Backend Flow
- /query → full book RAG
- /query-selected → selected text RAG

## Styling
- CSS Grid or Flexbox layout
- Sticky chat panel (optional)
- Responsive:
  - Desktop → side panel
  - Mobile → bottom panel

## Deployment
- Frontend bundled with Docusaurus
- Backend separate
```

## Response snapshot

Successfully completed the implementation planning workflow for the Book-Side RAG Chatbot:

1. Created comprehensive implementation plan (plan.md) with technical context, constitution check, and project structure
2. Completed research phase (research.md) with technical decisions and rationale
3. Designed data model (data-model.md) with 4 key entities (Book Content, User Query, Chat Response, Selected Text)
4. Generated API contracts (contracts/openapi.yaml) with complete OpenAPI specification for /query and /query-selected endpoints
5. Created quickstart guide (quickstart.md) with setup and deployment instructions
6. Updated agent context in QWEN.md with new technologies
7. Verified compliance with all 6 core principles from the constitution both pre-design and post-design

All artifacts are complete and the plan is ready for the next phase: /sp.tasks to break the plan into specific implementation tasks.

## Outcome

- ✅ Impact: Complete technical plan created for Book-Side RAG Chatbot
- 🧪 Tests: none
- 📁 Files: Created 6 files across multiple categories (plan, research, data model, contracts, quickstart, agent context)
- 🔁 Next prompts: /sp.tasks to break plan into implementation tasks
- 🧠 Reflection: Plan fully complies with constitution and technical requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A