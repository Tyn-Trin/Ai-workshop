import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()


def ask_claude(message: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.content[0].text
