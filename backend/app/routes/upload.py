import os
import shutil

from fastapi import APIRouter, UploadFile, File

from app.services.rag_service import ingest_document

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    upload_dir = "backend/data/documents"

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = ingest_document(file_path)

    return result