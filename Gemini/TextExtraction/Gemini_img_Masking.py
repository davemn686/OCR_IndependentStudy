import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('input_image.jpg')

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
kernel = np.ones((3, 3), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Step 6: Invert the morphological image to get black letters on a white background
inverted_morph = cv2.bitwise_not(morph)

# Step 7: Create a white mask
mask = np.ones_like(image) * 255  # Start with a white mask

# Step 8: Use the inverted image to define where to show the letters
mask[inverted_morph == 255] = [0, 0, 0]  # Set letter areas to black

# Show the result
cv2.imshow('Original Image', image)
cv2.imshow('morphology', morph)
cv2.imshow('Black Letters on White Background', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the result
cv2.imwrite('masked_image.png', mask)
