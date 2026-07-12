from app.utils.pdf_loader import load_pdf
from app.utils.text_splitter import split_text
from app.services.embedding_service import create_embedding
from app.services.vector_service import (
    create_collection,
    store_embeddings,
)


def ingest_document(file_path: str):
    # Step 1: Read PDF
    text = load_pdf(file_path)

    # Step 2: Split into chunks
    chunks = split_text(text)

    # Step 3: Generate embeddings
    embeddings = [create_embedding(chunk) for chunk in chunks]

    # Step 4: Create Qdrant collection
    create_collection(len(embeddings[0]))

    # Step 5: Store vectors
    store_embeddings(chunks, embeddings)

    return {
        "status": "success",
        "chunks": len(chunks)
    }