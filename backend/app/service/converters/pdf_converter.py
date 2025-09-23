from .base import DocumentToImage 
import pymupdf
import os

class PdfToImage(DocumentToImage):
    def convert(self, filepath: str) -> str:
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"PDF file does not exist: {filepath}")

        # Prepare output folder
        output_folder = self._prepare_output_folder(filepath)

        try:
            with pymupdf.open(filepath) as pdf_doc:
                total_pages = pdf_doc.page_count

                if total_pages == 0:
                    raise ValueError("PDF has no pages")

                for i in range(total_pages):
                    page = pdf_doc.load_page(i)
                    pix = page.get_pixmap()
                    image_path = os.path.join(output_folder, f"page_{i+1}.png")
                    pix.save(image_path)

        except pymupdf.PyMuPDFError as e:
            raise RuntimeError(f"Failed to convert PDF {filepath}: {e}")

        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

        return f"Converted PDF {filepath} → {total_pages} images stored in {output_folder}"