import cv2

# Read the image
image = cv2.imread('input_image.jpg')

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Display the original image
cv2.imshow('Original Image', image)

# Display the ROI
cv2.imshow('Gray Scale img', gray_image)
	
# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
