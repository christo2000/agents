from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
from pathlib import Path
from app.service.converters.image_conventor import ImageConverter
from typing import List

router = APIRouter(prefix="/files", tags=["PDF"])


@router.post("/upload")
def upload_pdf(files: List[UploadFile] = File(...)):
    results = []
    
    for file in files:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=415, detail=f"Only PDF files are supported. {file.filename} is not a PDF")

        # Save uploaded file temporarily
        temp_file = Path("./temp") / file.filename
        temp_file.parent.mkdir(parents=True, exist_ok=True)

        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:
            converter = ImageConverter.get_converter(file.content_type)
            result = converter.convert(temp_file)
            results.append({"filename": file.filename, "result": result})
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Conversion failed for {file.filename}: {str(e)}")

    return {"message": "PDFs converted to images successfully", "results": results}
