import cv2 as cv
import matplotlib.pyplot as plt
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDLt7t45guqJn21t9XFJYG7CQJnfmlxsuw")
# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")


# Generate text with caching
def GenerateText(filePath):
    myfile = genai.upload_file(filePath)
    result = model.generate_content([
        myfile,
        "\n",
        "ONLY Return the text in the image, NOTHING ELSE. if there is no text return no"
    ])
    print(result)
    return result

def  GetText(filePath):

    # Read the image
    img = cv.imread(filePath)
    assert img is not None, "file could not be read, check with os.path.exists()"

    # Apply different blurring techniques
    blur = cv.blur(img, (10, 2))
    cv.imwrite('../../images/blur.png', blur)

    GaussianBlur = cv.GaussianBlur(img, (3, 3), 0)
    cv.imwrite('../../images/Gauss.png', GaussianBlur)

    median = cv.medianBlur(img, 3)
    cv.imwrite('../../images/median.png', median)

    Filterblur = cv.bilateralFilter(img, 9, 75, 75)
    cv.imwrite('../../images/filter.png', Filterblur)


    try:
        temp = GenerateText(filePath).text
        print("original : " + temp.text)

        temp = GenerateText("../../images/blur.png").text
        print("blur : " + temp.text)

        temp = GenerateText("../../images/Gauss.png").text
        print("gauss : " + temp.text)

        temp = GenerateText("../../images/median.png").text
        print("median : " + temp.text)

        temp = GenerateText("../../images/filter.png")
        print("filter : " + temp.text)
    except ValueError as ve:
        print("value error occured here")

    # Include the original image in the list
    titles = ['Original Image', 'Image Blur', 'Gaussian Blur', 'Median Blurring', 'Bilateral Filtering']
    images = [img, blur, GaussianBlur, median, Filterblur]

    # Create a subplot for 5 images (2 rows and 3 columns)
    plt.figure(figsize=(10, 8))
    for i in range(5):
        plt.subplot(2, 3, i + 1)  # Adjusted to accommodate 5 images
        plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])



    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()

main = "../../images"

#print("UUXVRs")
#imgPath = main + "/UUXVRs.png"
#GetText(imgPath)


print("4NNECI")
imgPath = main + "/4NNECI.png"
GetText(imgPath)

"""
print("U0X2tW")
imgPath = main + "/U0x2tW.png"
GetText(imgPath)
"""