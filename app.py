from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# Simple in-memory storage
# -----------------------------
memory = []

# -----------------------------
# Request model
# -----------------------------
class ChatRequest(BaseModel):
    message: str


# -----------------------------
# Home page (index.html)
# -----------------------------
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


# -----------------------------
# Chat API
# -----------------------------
@app.post("/chat")
async def chat(req: ChatRequest):
    user_msg = req.message

    # store memory
    memory.append(user_msg)

    # demo AI response (later real AI connect pannalam)
    reply = f"I remember you said: {user_msg}"

    return {
        "response": reply,
        "memory_count": len(memory)
    }


# -----------------------------
# Health check (optional)
# -----------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}

