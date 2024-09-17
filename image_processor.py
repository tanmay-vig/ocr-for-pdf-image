import pytesseract

# Set the location of the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

def handle_image(file_path):
    """Handles OCR for image files using Tesseract."""
    try:
        img = Image.open(file_path)
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)
        return f"Extracted text from image: {text[:1000]}..."  # Limit to 1000 characters for display
    except Exception as e:
        return f"Error processing image: {str(e)}"
