from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import io

# Set the path to the Tesseract executable if it's not already in your PATH
# For Windows, you might need to set the tesseract_cmd explicitly
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def handle_pdf(file_path):
    """Handles OCR for PDF files using PyPDF2 and Tesseract OCR."""
    try:
        # Read PDF file
        reader = PdfReader(file_path)
        text = ""

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            # Extract text if available (may not be reliable for scanned PDFs)
            text += page.extract_text() or ""
            # Extract images and apply OCR
            images = page.images
            for img in images:
                image_data = img['data']
                image = Image.open(io.BytesIO(image_data))
                text += pytesseract.image_to_string(image) + "\n"

        return text
    except Exception as e:
        return f"Error processing PDF: {str(e)}"
