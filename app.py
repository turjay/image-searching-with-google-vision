from flask import Flask, request, render_template
from google.cloud import vision
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Limit upload file size to 5 MB
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB

# Path to Google Vision API credentials JSON file
GOOGLE_CREDENTIALS_PATH = 'credentials/static-destiny.json'

# Check if the Google Vision API credentials file exists
if not os.path.exists(GOOGLE_CREDENTIALS_PATH):
    raise FileNotFoundError(
        f"Google Vision API credentials file not found at {GOOGLE_CREDENTIALS_PATH}. "
        "Please ensure the file is in the correct location."
    )

# Set the credentials path as an environment variable for Google Vision API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_CREDENTIALS_PATH

# Allowed file extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """
    Check if the uploaded file has a valid extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the main page where users can upload an image.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle the uploaded file, process it with Google Vision API, 
    and return the results to the user.
    """
    # Retrieve the file from the request
    file = request.files.get('file')
    
    # Check if a file was uploaded
    if not file:
        return "No file was uploaded!"

    # Validate the file type
    if not allowed_file(file.filename):
        return "Invalid file type! Please upload a PNG, JPG, or JPEG image."

    # Initialize Google Vision API client
    try:
        client = vision.ImageAnnotatorClient()
    except Exception as e:
        return f"Failed to initialize Google Vision API client: {str(e)}"

    # Process the file with Google Vision API
    try:
        # Read the file content
        content = file.read()
        image = vision.Image(content=content)

        # Perform label detection on the image
        response = client.label_detection(image=image)

        # Check for errors in the API response
        if response.error.message:
            return f"Google Vision API Error: {response.error.message}"

        # Extract labels from the API response
        labels = response.label_annotations
    except Exception as e:
        return f"An error occurred while processing the image: {str(e)}"

    # Save the uploaded file securely to the static/uploads directory
    try:
        image_filename = secure_filename(file.filename)
        upload_path = os.path.join('static/uploads', image_filename)

        # Ensure the upload directory exists
        os.makedirs(os.path.dirname(upload_path), exist_ok=True)

        # Save the file
        file.seek(0)  # Reset the file pointer
        file.save(upload_path)
    except Exception as e:
        return f"Failed to save the uploaded file: {str(e)}"

    # Render the results page with labels and the uploaded image
    return render_template('result.html', labels=labels, image_url=f'/static/uploads/{image_filename}')

if __name__ == '__main__':
    """
    Run the Flask application. 
    'host="0.0.0.0' makes the app accessible on all network interfaces, allowing access from other devices in the same network.
    'port=5000' specifies the port where the app will run (default Flask port).
    Debug mode is for development purposes only and should be disabled in production.
    Example: app.run(debug=True, host='0.0.0.0', port=5000)
    Note: Use this only for development, not for production (For debug mode and 0.0.0.0).
    """
    app.run(host='0.0.0.0', port=5000) 