---

description: "Task list for Book-Side RAG Chatbot implementation"
---

# Tasks: Book-Side RAG Chatbot

**Input**: Design documents from `/specs/002-book-side-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend directory structure per implementation plan
- [ ] T002 Initialize Python project with FastAPI dependencies in backend/
- [ ] T003 [P] Initialize TypeScript project with Docusaurus dependencies in root
- [ ] T004 [P] Configure linting and formatting tools for both frontend and backend
- [ ] T005 Setup Qdrant vector database connection in backend
- [ ] T006 [P] Configure environment variables for API keys and service URLs

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T007 Setup backend main application entrypoint in backend/main.py
- [ ] T008 [P] Create base models for UserQuery and ChatResponse in backend/models/
- [ ] T009 [P] Create base models for BookContent and SelectedText in backend/models/
- [ ] T010 Setup API routing structure in backend/api/v1/
- [ ] T011 Configure CORS and middleware for Docusaurus integration
- [ ] T012 Setup error handling and logging infrastructure in backend
- [ ] T013 Create frontend component directory structure in src/components/BookChatbot/
- [ ] T014 Setup Docusaurus theme override at src/theme/DocItem/Layout.tsx

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Chatbot Beside Content (Priority: P1) 🎯 MVP

**Goal**: As a reader, I see the chatbot next to the book content so I can ask questions while reading without losing focus on the material.

**Independent Test**: Can be fully tested by loading a book page and verifying the chatbot appears in the designated position (right-side panel or below content) without requiring any user interaction beyond page load.

### Implementation for User Story 1

- [x] T015 [P] [US1] Create BookChatbot component in src/components/BookChatbot/BookChatbot.tsx
- [x] T016 [P] [US1] Create ChatWindow component in src/components/BookChatbot/ChatWindow.tsx
- [x] T017 [P] [US1] Create ChatInput component in src/components/BookChatbot/ChatInput.tsx
- [x] T018 [US1] Implement CSS Grid layout for book content + chatbot in BookChatbot.tsx
- [x] T019 [US1] Integrate BookChatbot with Docusaurus theme override in src/theme/DocItem/Layout.tsx
- [x] T020 [US1] Add responsive design for mobile (bottom panel) in BookChatbot.tsx
- [x] T021 [US1] Ensure non-overlapping layout with book content
- [x] T022 [US1] Add light/dark theme compatibility to chatbot components

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Ask Questions Without Leaving Page (Priority: P1)

**Goal**: As a student, I can ask questions without leaving the page so I can maintain my learning flow and context.

**Independent Test**: Can be fully tested by typing a question in the chat interface and submitting it, then verifying that the response appears without navigating away from the current page.

### Implementation for User Story 2

- [x] T023 [P] [US2] Implement query API endpoint in backend/api/v1/query.py
- [x] T024 [P] [US2] Create RAG service for full-book queries in backend/services/rag_service.py
- [x] T025 [US2] Connect frontend ChatInput to backend /query endpoint
- [x] T026 [US2] Implement chat message display in ChatWindow component
- [x] T027 [US2] Add loading states and error handling for queries
- [x] T028 [US2] Ensure original book content remains visible during chat interactions

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Highlight Text and Ask Questions (Priority: P2)

**Goal**: As a learner, I can highlight text from the book and send it as context to the chatbot so I can get specific answers about particular content.

**Independent Test**: Can be fully tested by selecting text in the book content, sending it to the chatbot, and verifying that the response considers the selected text as context.

### Implementation for User Story 3

- [x] T029 [P] [US3] Create useSelection hook in src/components/BookChatbot/useSelection.ts
- [x] T030 [P] [US3] Implement query-selected API endpoint in backend/api/v1/query.py
- [x] T031 [P] [US3] Enhance RAG service for selected-text queries in backend/services/rag_service.py
- [x] T032 [US3] Integrate text selection hook with ChatInput component
- [x] T033 [US3] Add visual indication of selected text in the UI
- [x] T034 [US3] Ensure selected text is properly sent as context with queries

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Verify Answers Are Book-Based (Priority: P2)

**Goal**: As a reviewer, I can verify that answers are based on the book content so I can trust the accuracy of the information provided.

**Independent Test**: Can be fully tested by asking questions about specific book topics and verifying that responses reference or are consistent with book content.

### Implementation for User Story 4

- [ ] T035 [P] [US4] Enhance ChatResponse model to include source citations
- [ ] T036 [P] [US4] Update RAG service to return source document references
- [ ] T037 [US4] Display source citations in ChatResponse component
- [ ] T038 [US4] Add confidence scoring to responses in backend
- [ ] T039 [US4] Implement handling for questions that cannot be answered from book content
- [ ] T040 [US4] Add visual indicators for response confidence and source reliability

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T041 [P] Documentation updates in docs/
- [ ] T042 Code cleanup and refactoring
- [ ] T043 Performance optimization across all stories
- [ ] T044 [P] Additional unit tests in backend/tests/unit/ and frontend tests
- [ ] T045 Security hardening
- [ ] T046 Run quickstart.md validation
- [ ] T047 Add accessibility features to chatbot UI components
- [ ] T048 Implement rate limiting and usage tracking

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Create BookChatbot component in src/components/BookChatbot/BookChatbot.tsx"
Task: "Create ChatWindow component in src/components/BookChatbot/ChatWindow.tsx"
Task: "Create ChatInput component in src/components/BookChatbot/ChatInput.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence