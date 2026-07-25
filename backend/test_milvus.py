import os
from dotenv import load_dotenv
from pymilvus import connections

load_dotenv()

connections.connect(
    alias="default",
    uri=os.getenv("MILVUS_URI"),
    token=os.getenv("MILVUS_TOKEN")
)

print("Connected successfully!")