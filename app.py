from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
from openai import OpenAI

# ----------------------------
# OpenAI Client
# ----------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI()

# ----------------------------
# Request Model
# ----------------------------
class ChatRequest(BaseModel):
    message: str

# ----------------------------
# Home Page
# ----------------------------
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# ----------------------------
# Chat API (REAL AI)
# -------…


