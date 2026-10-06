from fastapi import APIRouter
from pydantic import BaseModel
from app.services.memory_service import analyze_and_save_memory

from app.services.gemini_service import generate_response


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = generate_response(
    user_id="user_001",
    message=request.message,
)

    return ChatResponse(response=answer)