from captcha.image import ImageCaptcha
import random
import string

# Function to generate a random string of letters and digits
def generate_random_text(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to create a CAPTCHA image
def generate_captcha(text=None):
    image_captcha = ImageCaptcha(width=280, height=90)
    
    if text is None:
        text = generate_random_text()

    image = image_captcha.generate_image(text)
    image.show()  # Display the CAPTCHA image (optional)
    
    # Save the image to a file
    image.save(f"../../images/{text}.png")
    print(f"CAPTCHA for '{text}' saved as {text}.png")

# Generate and save a CAPTCHA image
if __name__ == "__main__":
    generate_captcha()
