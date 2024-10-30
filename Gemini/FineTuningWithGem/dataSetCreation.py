import os
from PIL import Image, ImageDraw, ImageFont
import random
import string

# Define dataset directory
dataset_dir = 'ocr_dataset/'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Update the path to point to your system's fonts directory
font_dir = r"C:\Windows\Fonts"  # Use raw strings (r"") for Windows paths

# Load available fonts
fonts = [os.path.join(font_dir, font_name) for font_name in os.listdir(font_dir) if font_name.endswith('.ttf')]

# Function to create random text
def random_text(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Function to generate image with text
def generate_image(text, img_width=256, img_height=64):
    # Choose a random font and size
    font_path = random.choice(fonts)
    font_size = random.randint(20, 40)
    font = ImageFont.truetype(font_path, font_size)

    # Create a blank white image
    img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    
    # Initializes drawing on the image
    d = ImageDraw.Draw(img)

    # Add text to the image
    ## Get the bounding box of the text
    bbox = d.textbbox((0, 0), text, font=font)
    ## Extracts the width and height of the text from the bouded box
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    ## Centers text in the image
    position = ((img_width - text_width) // 2, (img_height - text_height) // 2) 
    ## Draws text onto the image
    d.text(position, text, fill=(0, 0, 0), font=font)

    return img

# Generate the dataset
for i in range(10):  # Change to the desired dataset size
    text = random_text(random.randint(5, 15))  # Random text of random length
    img = generate_image(text)
    
    # Save the image
    img.save(f"{dataset_dir}/image_{i}.png")
    
    # Save the corresponding text label
    with open(f"{dataset_dir}/label_{i}.txt", "w") as f:
        # Write the random text to the file
        f.write(text)

print("Dataset generated!")

