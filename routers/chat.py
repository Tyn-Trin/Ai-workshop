from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.claude_service import ask_claude, ask_claude_with_rag

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest) -> ChatResponse:
    reply = ask_claude(request.message)
    return ChatResponse(reply=reply)


@router.post("/chat/rag")
def chat_rag(request: ChatRequest) -> ChatResponse:
    reply = ask_claude_with_rag(request.message)
    return ChatResponse(reply=reply)
