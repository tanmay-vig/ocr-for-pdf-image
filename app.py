import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from image_processor import handle_image
from pdf_processor import handle_pdf

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        # Initialize response content
        final_response = ""

        # Handle text input (description)
        if request.form.get('text_input'):
            text_input = request.form['text_input']
            final_response += f"Received text input: {text_input[:500]}\n\n"  # Limit response to 500 characters

        # Handle file input (PDF/image)
        if 'file_input' in request.files:
            file = request.files['file_input']
            if file and allowed_file(file.filename):
                # Secure the filename and save it to the uploads folder
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Process the uploaded file
                if filename.lower().endswith('.pdf'):
                    file_response = handle_pdf(file_path)
                elif filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    file_response = handle_image(file_path)
                else:
                    file_response = "Unsupported file format."

                # Add file response to final response
                final_response += f"Extracted content from file: {file_response}\n"

        # If neither text input nor file is provided
        if not final_response:
            final_response = "No text input or file uploaded."

        response = final_response

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
