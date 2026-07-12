from fastapi import FastAPI
from pydantic import BaseModel

# Import the upload router
from app.routes.upload import router as upload_router

app = FastAPI(title="RAG Chatbot API")


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


# Register the upload route
app.include_router(upload_router)