import os
from dotenv import load_dotenv
from pymilvus import MilvusClient

load_dotenv()

client = MilvusClient(
    uri=os.getenv("MILVUS_URI"),
    token=os.getenv("MILVUS_TOKEN")
)

COLLECTION_NAME = "documents"


def create_collection(vector_size: int):

    collections = client.list_collections()

    if COLLECTION_NAME not in collections:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            dimension=vector_size
        )


def store_embeddings(chunks, embeddings):

    data = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        data.append(
            {
                "primary_key": i,
                "embedding": embedding,
                "text": chunk
            }
        )

    client.insert(
        collection_name=COLLECTION_NAME,
        data=data
    )


def search_embeddings(query_embedding, limit=5):

    results = client.search(
        collection_name=COLLECTION_NAME,
        data=[query_embedding],
        limit=limit,
        output_fields=["text"]
    )

    chunks = []

    for hit in results[0]:
        chunks.append(hit["entity"]["text"])

    return chunks