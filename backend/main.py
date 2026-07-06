from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Welcome to my RAG Chatbot!"}


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "response": f"You said: {request.message}"
    }