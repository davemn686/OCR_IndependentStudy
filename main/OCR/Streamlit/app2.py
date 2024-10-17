import os
from google.cloud import vision

# Set up your Google Cloud Vision client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service-account-file.json'
client = vision.ImageAnnotatorClient()

def detect_text(image_path):
    """Detects text in an image file."""
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform text detection on the image
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f'{response.error.message}')

    # Print the detected text
    for text in texts:
        print(f'Detected text: {text.description}')

# Replace 'path/to/your/image.jpg' with the path to your image file
detect_text('path/to/your/image.jpg')
