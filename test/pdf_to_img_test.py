from pathlib import Path

from service.pdf_to_img import Pdf2Img

def main():
    pdf_path = r"C:\Users\HOME\Downloads\InJPharPract-16-3-191 (1) (1).pdf"
    ROOT_DIR = str(Path(__file__).parent.parent)+'/output'  # Adjust `.parent` levels if needed
    print(ROOT_DIR)
    pdf2img = Pdf2Img(pdf_path, output_dir=ROOT_DIR)
    pages_text = pdf2img.parse_and_save()
    return pages_text

if __name__ == "__main__":
    res = main()