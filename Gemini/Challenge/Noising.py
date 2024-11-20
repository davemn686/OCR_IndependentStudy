import cv2
import numpy as np

def add_noise(image_path, noise_type="gaussian", intensity=25):
    """
    Add noise to an image
    noise_type: "gaussian", "salt_pepper", or "poisson"
    intensity: Amount of noise (0-100 for gaussian, 0-0.1 for salt_pepper)
    """
    # Read the image
    image = cv2.imread(image_path)
    
    if noise_type == "gaussian":
        # Generate Gaussian noise
        mean = 0
        noise = np.random.normal(mean, intensity, image.shape).astype(np.uint8)
        noisy_image = cv2.add(image, noise)
        
    elif noise_type == "salt_pepper":
        # Generate Salt & Pepper noise
        noisy_image = image.copy()
        # Salt noise
        salt = np.random.random(image.shape) < intensity/2
        noisy_image[salt] = 255
        # Pepper noise
        pepper = np.random.random(image.shape) < intensity/2
        noisy_image[pepper] = 0
        
    elif noise_type == "poisson":
        # Generate Poisson noise
        noise = np.random.poisson(image).astype(np.uint8)
        noisy_image = image + noise
        
    return noisy_image

def save_noisy_image(input_path, output_path, noise_type="gaussian", intensity=25):
    """
    Add noise to an image and save it
    """
    noisy_image = add_noise(input_path, noise_type, intensity)
    cv2.imwrite(output_path, noisy_image)
    return output_path

input_image = "../../images/objects.jpg"

for i in range(10):    
    intensity = round((i + 1) * 0.1, 2)
    output_path = f"images/noisy_objects_salt_pepper_{intensity}.jpg"  # Add intensity to filename
    save_noisy_image(input_image, output_path, noise_type="salt_pepper", intensity=intensity)