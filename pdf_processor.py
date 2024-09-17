import os
import ocrmypdf
from PyPDF2 import PdfReader

def handle_pdf(file_path, upload_folder):
    """Handles OCR for PDF files using Tesseract."""
    try:
        ocr_output_path = os.path.join(upload_folder, 'ocr_' + os.path.basename(file_path))
        # Use ocrmypdf to process the PDF and apply OCR
        ocrmypdf.ocr(file_path, ocr_output_path, deskew=True)

        # Extract text from the OCR-processed PDF
        reader = PdfReader(ocr_output_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return f"Extracted text from PDF: {text[:1000]}..."  # Limit to 1000 characters for display
    except Exception as e:
        return f"Error processing PDF: {str(e)}"
