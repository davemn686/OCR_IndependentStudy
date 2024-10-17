
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones((5,5),np.uint8)

dilation = cv.dilate(img,kernel,iterations = 1)
erosion = cv.erode(img,kernel,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


# Create a list of the image titles and corresponding image data
images = [("Dilated", dilation),
          ("Eroded", erosion),
          ("Opening", opening),
          ("Closing", closing),
          ("Top Hat", tophat),
          ("Black Hat", blackhat)]

# Set up the matplotlib figure with a 2x3 grid
fig, axs = plt.subplots(2, 3, figsize=(10, 7))

# Loop through the images and display them in the grid
for i, (title, img) in enumerate(images):
    row, col = divmod(i, 3)  # Determine row and column for subplot
    axs[row, col].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # Convert image from BGR to RGB
    axs[row, col].set_title(title)
    axs[row, col].axis('off')  # Hide the axes

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
