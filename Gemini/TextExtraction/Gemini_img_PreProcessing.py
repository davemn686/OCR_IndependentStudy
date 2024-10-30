import cv2
import numpy as np

# Step 1: Read the image
#image = cv2.imread('input_image.jpg')
image = cv2.imread('TestWritten.png')

# Step 2: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian blur to smooth the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Use adaptive thresholding
thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               11, 2)

# Step 5: Apply morphological operations to enhance the letters
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Step 6: Apply noise removal using morphological opening (erosion followed by dilation)
opening_kernel = np.ones((1, 1), np.uint8)
morphology_noiseRemoval_1 = cv2.morphologyEx(morph, cv2.MORPH_OPEN, opening_kernel)

cv2.imshow('Morphology 1', morphology_noiseRemoval_1)

morphology_noiseRemoval_2 = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, opening_kernel)

cv2.imshow('Morphology 2', morphology_noiseRemoval_2)

morphology_noiseRemoval_3 = cv2.morphologyEx(morphology_noiseRemoval_1, cv2.MORPH_CLOSE, opening_kernel)

cv2.imshow('Morphology 3', morphology_noiseRemoval_3)

# Step 7: Invert the morphological image to get black letters on a white background
inverted_morph = cv2.bitwise_not(morphology_noiseRemoval_1)

# Show the result
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
