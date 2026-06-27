import os
from anthropic import Anthropic
from dotenv import load_dotenv
from services.rag_service import search_documents

load_dotenv()

client = Anthropic()

conversation_history = []

SYSTEM_PROMPT = "คุณคือ AI Assistant ที่ช่วยเรื่อง Odoo ERP ตอบเป็นภาษาไทย และกระชับ"


def ask_claude(message: str) -> str:
    conversation_history.append({"role": "user", "content": message})
    
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    reply = response.content[0].text
    conversation_history.append({"role": "assistant", "content": reply})

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

