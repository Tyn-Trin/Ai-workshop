import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))


class Base(DeclarativeBase):
    pass


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(20))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)


def save_message(role: str, content: str):
    with Session(engine) as session:
        message = ChatHistory(role=role, content=content)
        session.add(message)
        session.commit()


def get_history() -> list[dict]:
    with Session(engine) as session:
        messages = session.query(ChatHistory).order_by(ChatHistory.id).all()
        return [{"role": m.role, "content": m.content} for m in messages]
