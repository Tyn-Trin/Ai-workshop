from fastapi import FastAPI
from routers.chat import router as chat_router
from routers.documents import router as documents_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(documents_router)
