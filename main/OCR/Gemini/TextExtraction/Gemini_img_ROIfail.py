import google.generativeai as genai
import numpy as np
import cv2 as cv
import re
import time

# Configure the API key
genai.configure(api_key="AIzaSyDLt7t45guqJn21t9XFJYG7CQJnfmlxsuw")
model = genai.GenerativeModel("gemini-1.5-flash")

filePath = "..\\images\\HandWritten.png"

img = cv.imread(filePath)
height, width = img.shape[:2]
print(f"height = {height}")
print(f"width = {width}")


# Generate coordinates with caching
def GenerateCoordinates(filePath):
    myfile = genai.upload_file(filePath)
    result = model.generate_content([
        myfile,
        "\n",
        "Analyze the image and identify the coordinates of the text. Once you find the text, please return the rectangular region of interest in the format [y1:y2, x1:x2]. " +
        "Make sure the region is within the image bounds which is height:{height}, width:{width} , and adjusts according to the image size. only return one set of cordinates please"
    ])
    
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

def run(filePath):
    try:
        time.sleep(3)
        cordinates = GenerateCoordinates(filePath)
        text = GenerateText(filePath)
        
        print(f'Image text is: {text}')
        print(f'Text Coordinates are: {cordinates}')

        # Using regular expression to extract numbers
        numbers = re.findall(r'\d+', cordinates)
            
        if len(numbers) != 4:
            print("Not enough coordinates, ...Rerunning")
            run(filePath)
            
        # Convert extracted numbers to integers
        y1, y2, x1, x2 = map(int, numbers)
        print(x1, y1, x2, y2)
            
        # Now extract the ROI, ensuring coordinates are within image bounds
        if 0 <= y1 < y2 <= img.shape[0] and 0 <= x1 < x2 <= img.shape[1]:
            # Resizing image with OpenCV ROI
            roi = img[y1:y2, x1:x2]
            # Display the ROI
            cv.imshow('ROI Image', roi)
            # Write image to file
            newFilePath = f'..\\images\\roi_image1.jpg'
            cv.imwrite(newFilePath, roi)

            # Check if the ROI contains text
            ROI_Text = GenerateText(newFilePath)
            print(f"ROI Text: {ROI_Text}")
            
            if ROI_Text == "no":
                print("No text in ROI image, ...Rerunning")
                run(filePath)
            elif ROI_Text == text:
                print("Both texts are equal")
            else:
                print("Wrong text output, ...Rerunning")
                run(filePath)

        else:
            print(f"Coordinates out of bounds in iteration, ...Rerunning")
            run(filePath)
        
    except Exception as e:
        print(f"Error in iteration, ...Rerunning")
        run(filePath)

run(filePath)

# Display Original img
cv.imshow('Original Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
