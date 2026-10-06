# Nithish AI

A personal Agentic AI assistant, built incrementally as a learning project.

Planned stack: Python, FastAPI, React, Google Cloud Platform, Gemini (Google Agent Platform), Google Gen AI SDK, Google ADK and/or LangGraph, RAG, embeddings, vector search, Firestore, Cloud Storage, MCP, Docker, and Cloud Run.

## Current status

Only the project skeleton and a minimal FastAPI backend exist. No AI functionality yet.

## Run the backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Endpoints: `GET /` and `GET /health`.

See [docs/architecture.md](docs/architecture.md) for the intended architecture.
