from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router


app = FastAPI(
    title="Nithish AI",
    description="Personal Agentic AI Assistant",
    version="0.1.0",
)

# Wildcard origins are for deployment testing; restrict to the frontend URL later.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Welcome to Nithish AI"}


@app.get("/health")
def health():
    return {"status": "healthy"}


app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"],
)