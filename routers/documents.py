from fastapi import APIRouter
from pydantic import BaseModel
from services.rag_service import add_document

router = APIRouter()


class DocumentRequest(BaseModel):
    id: str
    text: str


@router.post("/documents")
def upload_document(request: DocumentRequest):
    add_document(request.id, request.text)
    return {"message": f"บันทึกเอกสาร '{request.id}' สำเร็จ"}
