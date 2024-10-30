import cv2

# Read the image
image = cv2.imread('input_image.jpg')

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image")
    exit()

# Define the Region of Interest (ROI)
# Let's assume we want to select a rectangular region
# Example coordinates: [y1:y2, x1:x2] (y is for rows, x is for columns)
roi = image[29:201, 20:355]  # This will select a 200x200 region starting from (200, 100)

# Display the original image
cv2.imshow('Original Image', image)

# Display the ROI
cv2.imshow('ROI', roi)

# Save the ROI as a separate image
cv2.imwrite('roi_image.jpg', roi)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
