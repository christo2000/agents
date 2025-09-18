from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
from pathlib import Path
from app.service.pdf_service import PdfService

router = APIRouter(prefix="/files", tags=["PDF"])


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Only PDF files are supported")

    # Save uploaded file temporarily
    temp_file = Path("./temp") / file.filename
    temp_file.parent.mkdir(parents=True, exist_ok=True)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #PDF -> images
    pdf_service = PdfService(pdf_path=temp_file)
    result = pdf_service.pdf_to_images()

    return {"message": "PDF converted to images successfully", "result": result}
