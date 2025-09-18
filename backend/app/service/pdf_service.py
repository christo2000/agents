import pdfplumber
from pathlib import Path
import uuid


class PdfService:
    def __init__(self, pdf_path, output_dir="./output"):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir) / uuid.uuid4().hex
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def pdf_to_images(self):
        saved_images = []

        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                img_path = self.output_dir / f"page_{i+1}.png"
                pil_img = page.to_image(resolution=150).original
                pil_img.save(img_path)
                saved_images.append(str(img_path))

        return {
            "pdf_file": str(self.pdf_path),
            "pages": len(saved_images),
            "saved_images": saved_images,
            "output_dir": str(self.output_dir)
        }
