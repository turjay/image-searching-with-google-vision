# Image Searching with Google Vision

#### Video Demo: https://youtu.be/2Ta25ebazW8

#### Description:

This project leverages the **Google Vision API** to perform image analysis by detecting labels (objects, people, places, etc.) in an image. The primary objective of this project is to help users upload images and receive relevant information about the content of the images. The backend is built with **Flask** (Python), and the frontend uses **HTML**, **CSS**, and **JavaScript** to create an intuitive user interface.

The project utilizes the **Google Cloud Vision API**, which is capable of detecting a wide variety of features in images, including but not limited to label detection, face detection, landmark recognition, and optical character recognition (OCR).

## Technologies Used:
- **Python**: For backend logic.
- **Flask**: A Python web framework to handle HTTP requests.
- **Google Cloud Vision API**: To analyze the content of the uploaded images.
- **HTML/CSS**: To create a simple user interface for image uploads and displaying analysis results.
- **JavaScript**: To handle dynamic operations, such as submitting the image for analysis without reloading the page.

## Project Files:

- `app.py`: Contains the Flask application and the backend logic to handle requests and communicate with the Google Vision API.
- `static/css/style.css`: The stylesheet used to style the page.
- `static/js/script.js`: JavaScript used for dynamic operations like image upload and result display.
- `templates/index.html`: The HTML file where users can upload images.
- `templates/result.html`: The HTML file that displays the results of the image analysis.

## Design Choices:

In designing this project, I wanted to create a simple and clean user interface that could be easily navigated. I chose **Flask** for the backend because of its lightweight nature, which is perfect for small-scale applications like this one. I also chose to use the **Google Cloud Vision API** because it provides powerful image analysis capabilities with minimal setup.

### Why Flask?
Flask is a micro web framework for Python that is lightweight and easy to use. I found it ideal for this project because I wanted to focus on the application logic rather than dealing with the complexity of larger frameworks. Flask is simple and provides the flexibility needed for this project.

### Why Google Vision API?
The **Google Vision API** allows developers to build intelligent applications that can "see" and analyze images. I chose this API because it supports various types of image recognition tasks (e.g., label detection, landmark recognition) and is relatively easy to implement within a Python Flask application.

## Setup:

To run this project locally, follow the steps below.

1. Create a Virtual Environment (Optional but Recommended):
    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:
    - On **Linux/Mac**
        ```bash
        source venv/bin/activate
        ```
        - On Windows
        ```bash
        .\venv\Scripts\activate
        ```
    If you want to deactivate the virtual environment later, simply run:
    ```bash
    deactivate
    ```

2. Install the Necessary Dependencies:

    To use the Google Vision API, you must create your own credentials JSON file. Follow these steps:

    1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
    2. Create a new project and enable the **Vision API.**
    3. Navigate to the **APIs & Services > Credentials > Create Credentials** section.
    4. Create a service account and download the JSON key file.
    5. Place the downloaded JSON file in the credentials/ folder of the project directory.
    6. Rename the file (if needed) to match the name used in the project code, e.g., credentials/static-destiny.json.

This will start the application on `http://127.0.0.1:5000`, where you can upload images for analysis.

## Usage:

1. After running the Flask app, open your browser and go to `http://127.0.0.1:5000`.
2. On the homepage, you will see an option to upload an image. Select any image from your local system.
3. The image will be sent to the backend, which will use the Google Vision API to analyze it.
4. The detected labels (objects, scenes, and other content) will be displayed on the results page.

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

**This project does not include a default Google API credentials file. You must create and configure your own credentials as described above.**