import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('TestWritten.png')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.blur(img,(20,10))

GaussianBlur = cv.GaussianBlur(img,(9,9),0)

median = cv.medianBlur(img,9)

Filterblur = cv.bilateralFilter(img,9,75,75)


titles = ['image blur',
            'Gaussian Blur', 'Median Blurring','Bilateral Filtering']
images = [blur, GaussianBlur, median, Filterblur, img]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
