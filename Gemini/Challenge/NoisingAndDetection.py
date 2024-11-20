import ObjectDetection
import Noising




#filePath = "images/noisy_objects_salt_pepper.jpg"
#ObjectDetection.DetectingObjects(filePath)

input_image = "../../images/objects.jpg"
output_image = "images/noisy_objects_gaussian.jpg"
output_image2 = "images/noisy_objects_salt_pepper.jpg"
output_image3 = "images/noisy_objects_poisson.jpg"

# Iterate with increasing intensity from 10 to 100
for i in range(10):    
    intensity = (i + 1) * 10  # This will give: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    output_path = f"images/noisy_objects_gaussian_{intensity}.jpg"  # Add intensity to filename
    Noising.save_noisy_image(input_image, output_path, noise_type="gaussian", intensity=intensity)
    ObjectDetection.DetectingObjects(output_path)



#Noising.save_noisy_image(input_image, output_image2, noise_type="salt_pepper", intensity=0.25)

#Noising.save_noisy_image(input_image, output_image3, noise_type="poisson", intensity=75)
    
# For salt & pepper noise (use lower intensity, e.g., 0.05)
# Noising.save_noisy_image(input_image, output_image, noise_type="salt_pepper", intensity=0.05)

