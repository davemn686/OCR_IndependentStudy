import cv2

image_path = 'input_image.jpg'
image = cv2.imread(image_path)

if image is None:
	print(f"Error: could not load image from {image_path}")
else:
	cv2.imshow('Image Window', image)

	cv2.waitKey(0)

	cv2.destroyAllWindows()

	output_path = 'output_image.jpg'
	cv2.imwrite(output_path, image)
	
	#print(f"Image saved to {output_pastreth}")
