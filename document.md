# RAG Chatbot Project Documentation

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) Chatbot that allows users to upload PDF documents and ask questions about their content. The system processes the documents, splits them into manageable chunks, generates vector embeddings, and stores them in a Milvus vector database. When a user asks a question, the chatbot retrieves the most relevant document chunks based on semantic similarity and uses a Large Language Model (LLM) to generate an accurate answer based on the provided context.

## What is Done (Project Architecture)
The project is built with a backend-focused architecture containing the following components:

1. **API Endpoints (FastAPI)**:
   - `GET /`: Health check and welcome message.
   - `POST /upload`: Uploads a PDF file, saves it locally in `backend/data/documents`, extracts text, chunks it, creates embeddings, and stores them in the vector database.
   - `POST /chat`: Receives a user question, searches for relevant context in the vector database, and queries the LLM for an answer.

2. **Services**:
   - `rag_service.py`: Orchestrates the ingestion of documents and the question-answering workflow.
   - `vector_service.py`: Manages the connection to Milvus, creates collections, stores embeddings, and performs similarity searches.
   - `llm_service.py`: Connects to Google's Gemini API to answer questions using the retrieved context (`gemini-2.5-flash`).
   - `embedding_service.py`: Connects to Google's Gemini API to generate text embeddings (`gemini-embedding-001`).

3. **Utilities**:
   - `pdf_loader.py`: Handles reading and extracting text from PDF files.
   - `text_splitter.py`: Splits large text into smaller chunks suitable for embedding.

## Tech Stack
- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) - For building fast, modern RESTful APIs in Python.
- **Vector Database**: [Milvus](https://milvus.io/) (via `pymilvus`) - For storing and retrieving high-dimensional vector embeddings.
- **Large Language Model (LLM)**: [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) (via `google-genai`) - For text generation and contextual answering.
- **Embedding Model**: Google Gemini Embeddings (`gemini-embedding-001`) - For transforming text into vector representations.
- **Language**: Python

## How to Run the Project

### Prerequisites
Make sure you have Python installed, and you have set up your `.env` file in the `backend/` directory with the following variables:
```env
MILVUS_URI=your_milvus_uri
MILVUS_TOKEN=your_milvus_token
GEMINI_API_KEY=your_gemini_api_key
```

### Steps to Run
1. Open a terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate # On macOS/Linux
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI development server:
   ```bash
   uvicorn main:app --reload
   ```
5. The API will be available at `http://127.0.0.1:8000`. You can access the interactive API Swagger documentation at `http://127.0.0.1:8000/docs` to test the `/upload` and `/chat` endpoints.


cd D:\RAG-Chatbot\frontend
npm run dev