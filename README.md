
# Enterprise RAG Chatbot using FastAPI, Gemini & Milvus

## Overview

This project is an enterprise-style Retrieval-Augmented Generation (RAG) chatbot that enables users to upload PDF documents and ask context-aware questions. It combines Google's Gemini models for embedding generation and response generation with Milvus, an enterprise-grade vector database, to provide semantic document retrieval and accurate answers.

---

## Features

- Upload PDF documents for knowledge ingestion
- Automatic text extraction and intelligent chunking
- Semantic embeddings generated using Gemini Embedding Model
- Enterprise-grade vector storage using Milvus (Zilliz Cloud)
- Semantic similarity search for relevant context retrieval
- Context-aware responses powered by Gemini 2.5 Flash
- RESTful API built with FastAPI
- Interactive API documentation using Swagger UI

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Backend Framework | FastAPI |
| Programming Language | Python |
| Large Language Model | Gemini 2.5 Flash |
| Embedding Model | Gemini Embedding |
| Vector Database | Milvus (Zilliz Cloud) |
| PDF Processing | PyPDF2 |
| API Documentation | Swagger UI |
| Environment Management | python-dotenv |

---

# System Architecture

```
                   PDF Document
                        │
                        ▼
                 PDF Text Extraction
                        │
                        ▼
                 Text Chunking
                        │
                        ▼
              Gemini Embedding Model
                        │
                        ▼
           Milvus Vector Database
                        │
              Semantic Retrieval
                        │
                        ▼
              Retrieved Context
                        │
                        ▼
               Gemini 2.5 Flash
                        │
                        ▼
                  Final Response
```

---

# Project Structure

```
backend/
│
├── app/
│   ├── routes/
│   │   └── upload.py
│   │
│   ├── services/
│   │   ├── embedding_service.py
│   │   ├── vector_service.py
│   │   ├── rag_service.py
│   │   └── llm_service.py
│   │
│   └── utils/
│       ├── pdf_loader.py
│       └── text_splitter.py
│
├── data/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

### Clone the repository

```bash
git clone https://github.com/AshinaShaju/RAG-Chatbot.git
```

### Navigate to the backend

```bash
cd RAG-Chatbot/backend
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file inside the backend directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

MILVUS_URI=YOUR_MILVUS_URI

MILVUS_TOKEN=YOUR_MILVUS_TOKEN
```

### Start the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Upload Document

```
POST /upload
```

Uploads a PDF document, extracts its contents, generates embeddings, and stores them in the Milvus vector database.

---

## Ask Questions

```
POST /chat
```

Example Request

```json
{
    "message": "What is this document about?"
}
```

Example Response

```json
{
    "response": "The uploaded document discusses..."
}
```

---

# Workflow

### Document Ingestion

```
PDF Upload
      │
      ▼
Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Store Embeddings in Milvus
```

### Question Answering

```
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Search in Milvus
      │
      ▼
Retrieve Relevant Context
      │
      ▼
Generate Response using Gemini
      │
      ▼
Return Final Answer
```

---

# Future Enhancements

- Support multiple PDF documents
- Conversation memory
- Source citations and page references
- Hybrid search (keyword + semantic search)
- React-based frontend
- Docker containerization
- Cloud deployment (AWS/Azure/GCP)
- User authentication and authorization
- Role-based access control
- Conversation history management

---

# Author

**Ashina Shaju**

LinkedIn  
https://www.linkedin.com/in/ashina-shaju

GitHub  
https://github.com/AshinaShaju
