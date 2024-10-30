import google.generativeai as genai
import numpy as np
import cv2 as cv
import re

# Configure API key
genai.configure(api_key="AIzaSyDLt7t45guqJn21t9XFJYG7CQJnfmlxsuw")
# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
filePath = "../../../images/plate.jpg"


# Load the image
img = cv.imread(filePath)
height, width = img.shape[:2]
print(f"height = {height}")
print(f"width = {width}")


# Generates The cordinates of text
def GenerateCoordinates(filePath):
    myfile = genai.upload_file(filePath)
    prompt = "Return bounding boxes for text in the image. Format: [xmin, ymin, xmax, ymax]. Only provide one coordinates."
    result = model.generate_content([myfile, prompt])
    return result.text



# Generate text with caching
def GenerateText(filePath):
    myfile = genai.upload_file(filePath)
    result = model.generate_content([
        myfile,
        "\n",
        "ONLY Return the text in the image, NOTHING ELSE. if there is no text return no"
    ])
    
    return result.text

# Generate coordinates
text_coordinates = GenerateCoordinates(filePath)
print(f'Text Coordinates Returned: {text_coordinates}')

image_Text = GenerateText(filePath)
print(f'The text in the image is : {image_Text}')

# Using regex to extract numbers
numbers = re.findall(r'\d+', text_coordinates)

# Check if we have exactly 4 numbers for coordinates
ymin, xmin, ymax, xmax = map(int, numbers)

# Convert coordinates to original dimensions
xmin = int(xmin / 1000 * width)
ymin = int(ymin / 1000 * height)
xmax = int(xmax / 1000 * width)
ymax = int(ymax / 1000 * height)


# Draw a rectangle around the detected text position in the resized image
cv.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

# Display the original and resized images
cv.imshow('rectangle Image', img)

# Wait until a key is pressed and close the image windows
cv.waitKey(0)
cv.destroyAllWindows()
