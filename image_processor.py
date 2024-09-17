import pytesseract
from PIL import Image

# Set the location of the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def handle_image(file_path):
    """Handles OCR for image files using Tesseract OCR."""
    try:
        # Open the image file
        image = Image.open(file_path)
        
        # Use Tesseract to extract text
        text = pytesseract.image_to_string(image)
        
        return text
    except Exception as e:
        return f"Error processing image: {str(e)}"
