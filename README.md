# Odoo AI Python

AI Chat Service ที่เชื่อมต่อ Claude AI กับ Odoo

## Requirements

- Python 3.x
- Anthropic API Key ([สมัครได้ที่ console.anthropic.com](https://console.anthropic.com))

## การติดตั้ง

**1. Clone โปรเจกต์**
```bash
git clone https://github.com/Tyn-Trin/Ai-workshop.git
cd Ai-workshop
```

**2. สร้าง Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. ติดตั้ง Library**
```bash
pip install fastapi uvicorn anthropic python-dotenv
```

**4. สร้างไฟล์ .env**
```
ANTHROPIC_API_KEY=your_api_key_here
```

## การรัน

```bash
uvicorn main:app --reload
```

เปิด browser ไปที่ http://localhost:8000/docs

## โครงสร้างโปรเจกต์

```
├── main.py                     # Entry point
├── routers/
│   └── chat.py                 # API Routes
├── services/
│   └── claude_service.py       # Claude AI Logic
├── models/
│   └── schemas.py              # Request/Response Models
└── tools/                      # Claude Tool Definitions (Week 2+)
```
