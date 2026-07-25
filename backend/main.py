from fastapi import FastAPI
from pydantic import BaseModel

# Upload router
from app.routes.upload import router as upload_router

# Import RAG service
from app.services.rag_service import ask_question

app = FastAPI(title="RAG Chatbot API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Welcome to my RAG Chatbot!"}


@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_question(request.message)

    return {
        "response": answer
    }


# Register upload router
app.include_router(upload_router)