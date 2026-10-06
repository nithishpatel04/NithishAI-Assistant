# Nithish AI - Intended Architecture

This describes the planned design. None of it is implemented yet.

```
React
    ↓
FastAPI
    ↓
Nithish AI Agent
    ↓
Gemini / Google Agent Platform
    ↓
Tools + RAG + Memory + MCP
    ↓
GCP services
```

- **React**: chat UI.
- **FastAPI**: HTTP API layer.
- **Nithish AI Agent**: orchestrates reasoning (Google ADK and/or LangGraph).
- **Gemini / Google Agent Platform**: the LLM, accessed via the Google Gen AI SDK.
- **Tools + RAG + Memory + MCP**: function calling, retrieval over documents, persistent memory, and MCP integrations.
- **GCP services**: Cloud Storage (documents), Firestore (memory), vector search, Cloud Run (deployment).
