import os
import pdfplumber
from pathlib import Path

from service.image_handlers import ImageToBase64, FileImageReader


class Pdf2Img:
    def __init__(self, pdf_path, output_dir=str(Path(__file__).parent.parent) + "/output"):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.pdf_name = self.pdf_path.stem  # safer than removesuffix('.pdf')
        self.final_out_dir = self.output_dir / self.pdf_name
        self.final_out_dir.mkdir(parents=True, exist_ok=True)

    def parse_and_save(self):
        pdf_text_list = []
        pdf_metadata = {}

        try:
            if self.pdf_path.exists() and self.pdf_path.suffix.lower() == ".pdf":
                with pdfplumber.open(self.pdf_path) as pdf:
                    for i, page in enumerate(pdf.pages):
                        try:
                            # Extract text
                            page_text = page.extract_text() or ""
                            pdf_text_list.append({f"page_{i}": page_text})

                            # Save image
                            img_path = self.final_out_dir / f"page_{i}.png"
                            pil_img = page.to_image(resolution=150).original
                            pil_img.save(img_path)

                            print(f"✅ Saved page {i} text and image: {img_path}")
                        except Exception as e:
                            print(f"⚠️ Failed to process page {i}: {e}")

                    # Collect metadata
                    pdf_file_reader = FileImageReader(self.pdf_path)
                    img2base64 = ImageToBase64(pdf_file_reader)
                    pdf_metadata = {
                        "pdf_input_path" : self.pdf_path,
                        "pdf_name" : self.pdf_name,
                        "pdf_out_dir"  : self.final_out_dir,
                        "pdf_pages": len(pdf.pages),
                        "pdf_width": pdf.pages[0].width,
                        "pdf_height": pdf.pages[0].height,
                        "pdf_metadata": pdf.metadata,
                        "hash_value": hash(pdf),
                        "base64": img2base64.encode(),
                        "pdf_text": pdf_text_list,
                    }

                return pdf_metadata

            else:
                raise ValueError(f"Input is not a PDF: {self.pdf_path}")

        except Exception as e:
            print(f"❌ Error while parsing {self.pdf_path}: {e}")
            return None
