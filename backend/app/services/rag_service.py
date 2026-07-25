from app.utils.pdf_loader import load_pdf
from app.utils.text_splitter import split_text

from app.services.embedding_service import create_embedding

from app.services.vector_service import (
    create_collection,
    store_embeddings,
    search_embeddings,
)

from app.services.llm_service import ask_gemini


def ingest_document(file_path: str):
    # Read PDF
    text = load_pdf(file_path)

    # Split text
    chunks = split_text(text)

    # Create embeddings
    embeddings = [create_embedding(chunk) for chunk in chunks]

    # Create Qdrant collection
    create_collection(len(embeddings[0]))

    # Store vectors
    store_embeddings(chunks, embeddings)

    return {
        "status": "success",
        "chunks": len(chunks)
    }


def ask_question(question: str):

    # Create embedding of the question
    question_embedding = create_embedding(question)

    # Retrieve similar chunks
    retrieved_chunks = search_embeddings(question_embedding)

    # Merge chunks into one context
    context = "\n\n".join(retrieved_chunks)

    # Ask Gemini
    answer = ask_gemini(question, context)

    return answer