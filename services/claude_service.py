import os
from anthropic import Anthropic
from dotenv import load_dotenv
from services.rag_service import search_documents
from services.db_service import save_message, get_history

load_dotenv()

client = Anthropic()

SYSTEM_PROMPT = "คุณคือ AI Assistant ที่ช่วยเรื่อง Odoo ERP ตอบเป็นภาษาไทย และกระชับ"


def ask_claude(message: str) -> str:
    save_message("user", message)
    history = get_history()

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history
    )

    reply = response.content[0].text
    save_message("assistant", reply)

    return reply


def ask_claude_with_rag(message: str) -> str:
    docs = search_documents(message)
    context = "\n".join(docs)

    prompt = f"""ใช้ข้อมูลด้านล่างนี้ในการตอบคำถาม:

{context}

คำถาม: {message}"""

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

