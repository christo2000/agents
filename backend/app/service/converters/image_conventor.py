from .pdf_converter import PdfToImage
from .base import DocumentToImage

class ImageConverter:
    _converters = {
        "application/pdf": PdfToImage
    }

    @classmethod
    def get_converter(cls, file_type: str) -> DocumentToImage:
        file_type = file_type.lower()
        if file_type not in cls._converters:
            raise ValueError(f"Unsupported file type: {file_type}")
        return cls._converters[file_type]()
