from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# ---------- APP ----------
app = FastAPI(title="Memory AI Project")

# ---------- TEMPLATES ----------
templates = Jinja2Templates(directory="templates")

# ---------- WEBSITE (HOME PAGE) ----------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# ---------- SIMPLE API (CHECK) ----------
@app.get("/health")
def health():
    return {
        "status": "API is running successfully",
        "message": "Memory AI backend is live 🚀"
    }

# ---------- SAMPLE CHAT API ----------
@app.post("/chat")
def chat(data: dict):
    user_id = data.get("user_id")
    message = data.get("message")

    return {
        "user_id": user_id,
        "message": message,
        "response": "This is a demo response from Memory AI"
    }