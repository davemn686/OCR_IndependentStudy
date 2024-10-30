import cv2
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Load the image with OpenCV
img = cv2.imread('ANCharacter.jpg')

# Preprocess the image: Convert to grayscale and apply thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)


cv2.imshow('Grayscale image', thresh)

cv2.waitKey(0)  # Waits for a key press
cv2.destroyAllWindows()

# Convert the image to PIL format (needed by pytesseract)
img_pil = Image.fromarray(thresh)

# Extract text using pytesseract
text = pytesseract.image_to_string(img_pil)

# Postprocessing: Clean up the text
cleaned_text = text.strip().replace('\n', ' ')

# Print or save the extracted text
print(cleaned_text)
