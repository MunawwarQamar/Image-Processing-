import cv2
import numpy as np

def resize_image(image_path, new_width, new_height):
    # Read the image
    image = cv2.imread(image_path)

    # Get the original dimensions of the image
    original_height, original_width = image.shape[:2]

    # Create an empty array to store the resized image
    resized_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Calculate scaling factors for width and height
    width_scale = original_width / new_width
    height_scale = original_height / new_height

    # Iterate over each pixel in the resized image
    for y in range(new_height):
        for x in range(new_width):
            # Calculate the corresponding pixel coordinates in the original image
            x_original = int(x * width_scale)
            y_original = int(y * height_scale)

            # Copy the pixel value from the original image to the resized image
            resized_image[y, x] = image[y_original, x_original]

    return resized_image

image_path = 'grayscale.jpg'  
resized_image = resize_image(image_path, 256, 256)  # Resize to width=256 and height=256
cv2.imwrite('downscaled.jpg', resized_image)  # Save the resized image
cv2.imshow('downscaled.jpg', resized_image)  # Display the resized image
cv2.waitKey(0)
cv2.destroyAllWindows()