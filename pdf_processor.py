import subprocess
import os

def handle_pdf(file_path, upload_folder):
    """Handles OCR for PDF files using OCRmyPDF."""
    try:
        output_path = os.path.join(upload_folder, 'output.pdf')

        # Specify full paths for ocrmypdf and pdftotext
        ocrmypdf_path = r'C:\Path\To\ocrmypdf.exe'  # Update to the actual path of ocrmypdf.exe
        pdftotext_path = r'C:\Program Files\poppler\bin\pdftotext.exe'  # Update to the actual path of pdftotext.exe

        # Run OCRmyPDF with --force-ocr option
        result = subprocess.run([ocrmypdf_path, '--force-ocr', file_path, output_path],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check for errors in OCRmyPDF execution
        if result.returncode != 0:
            return f"Error processing PDF with OCRmyPDF: {result.stderr}"

        # Run pdftotext to extract text from output PDF
        text_result = subprocess.run([pdftotext_path, output_path, '-'],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check for errors in pdftotext execution
        if text_result.returncode != 0:
            return f"Error extracting text with pdftotext: {text_result.stderr}"

        os.remove(output_path)  # Clean up the output file
        return text_result.stdout  # Return extracted text
    except Exception as e:
        return f"Error processing PDF: {str(e)}"
