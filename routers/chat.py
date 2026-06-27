from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.claude_service import ask_claude

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest) -> ChatResponse:
    reply = ask_claude(request.message)
    return ChatResponse(reply=reply)
