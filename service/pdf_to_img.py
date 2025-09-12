import os

import pdfplumber
from pathlib import Path

from service.image_handlers import ImageToBase64, FileImageReader


class Pdf2Img:
    def __init__(self, pdf_path, output_dir="./output"):
        self.pdf_path = pdf_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def parse_and_save(self):
        pdf_text_list = []
        pdf_metadata = {}

        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                # Extract text
                page_text = page.extract_text() or ""
                pdf_text_list.append({f"page_{i}": page_text})

                # Save image
                img_path = self.output_dir / f"page_{i}.png"
                pil_img = page.to_image(resolution=150).original
                pil_img.save(img_path)

                print(f"Saved page {i} text and image: {img_path}")
            pdf_file_reader = FileImageReader(self.pdf_path)
            img2base64 = ImageToBase64(pdf_file_reader)
            pdf_metadata["pdf_pages"] = len(pdf.pages)
            pdf_metadata["pdf_width"] = pdf.pages[0].width
            pdf_metadata["pdf_height"] = pdf.pages[0].height
            pdf_metadata["pdf_metadata"] = pdf.metadata
            pdf_metadata["hash_value"] = hash(pdf)
            pdf_metadata["base64"] = img2base64.encode()
            pdf_metadata["pdf_text"] = pdf_text_list

        return pdf_metadata


if __name__ == "__main__":
    pdf_path = r"C:\Users\HOME\Downloads\InJPharPract-16-3-191 (1) (1).pdf"
    ROOT_DIR = str(Path(__file__).parent.parent)+'/output'  # Adjust `.parent` levels if needed
    print(ROOT_DIR)
    pdf2img = Pdf2Img(pdf_path, output_dir=ROOT_DIR)
    pages_text = pdf2img.parse_and_save()
    # print(pages_text)


