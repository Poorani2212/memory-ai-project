from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# ------------------ CORS ------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ Templates ------------------
templates = Jinja2Templates(directory=".")

# ------------------ Home Page ------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ------------------ Chat API ------------------
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    if not user_message:
        return JSONResponse({"reply": "Please type something"}, status_code=400)

    # Demo AI response (later real AI add pannalaam)
    reply = f"This is a demo response from Memory AI. You said: {user_message}"

    return {"reply": reply}

# ------------------ Health Check ------------------
@app.get("/health")
async def health():
    return {"status": "ok"}
