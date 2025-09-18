from fastapi import FastAPI
from app.api import files
from app.core.database import create_tables

create_tables()

app = FastAPI(title="Image Extraction")

# Include router
app.include_router(files.router, prefix="/api")
