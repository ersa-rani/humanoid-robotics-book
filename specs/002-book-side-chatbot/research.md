# Research: Book-Side RAG Chatbot

## Decision: Docusaurus Theme Override Approach
**Rationale**: Using Docusaurus theme override at `src/theme/DocItem/Layout.tsx` allows us to inject the chatbot component into every documentation page automatically, meeting the requirement that the chatbot appears on every page without user interaction.

**Alternatives considered**:
- Using a Docusaurus plugin: More complex setup, harder to customize layout
- Modifying each MDX file individually: Not maintainable, would require changes to all existing and future docs
- Using a Docusaurus preset: Less control over exact positioning and behavior

## Decision: CSS Grid Layout for Content + Chatbot
**Rationale**: CSS Grid provides the most flexible and responsive approach to arrange the book content and chatbot panel side-by-side, with the ability to switch to stacked layout on mobile devices.

**Alternatives considered**:
- Flexbox: Also viable but Grid offers better control for 2D layouts
- Absolute positioning: Would cause overlap issues and be harder to make responsive
- Iframe approach: Forbidden by constitution (no iframe embeds)

## Decision: FastAPI Backend with RAG Integration
**Rationale**: FastAPI provides excellent performance, automatic API documentation, and strong typing. Combined with Qdrant for vector storage and OpenAI agents for RAG, it creates a powerful backend for answering questions about the book content.

**Alternatives considered**:
- Node.js/Express: Would work but Python is more common for ML/AI applications
- Direct integration with OpenAI API: Less control over the RAG process
- Other Python frameworks (Flask): FastAPI offers better performance and documentation

## Decision: Text Selection Hook Implementation
**Rationale**: Creating a custom React hook `useSelection` will allow us to detect and capture text selections from the book content, which can then be sent as context with user queries.

**Alternatives considered**:
- Global event listeners: Could be harder to manage and scope properly
- Third-party libraries: Would add unnecessary dependencies when the functionality is straightforward
- Browser native APIs directly: Less reusable without the hook abstraction

## Decision: Responsive Design Strategy
**Rationale**: The chatbot will appear as a right-side panel on desktop and switch to a bottom panel on mobile devices to ensure usability across all screen sizes while maintaining visibility.

**Alternatives considered**:
- Collapsible sidebar: Would hide the chatbot, violating the "always visible" requirement
- Floating button: Forbidden by constitution (no hidden floating-only button)
- Separate mobile view: Would require navigation away from content