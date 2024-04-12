
import cv2
import numpy as np

def manual_invert_image(image):
    # Get the dimensions of the image
    height, width = image.shape

    # Create an empty array with the same size and data type as the image
    negative_image = np.zeros((height, width), dtype=np.uint8)

    # Iterate through each pixel in the image
    for i in range(height):
        for j in range(width):
            # Subtract the pixel value from 255 to invert it
            negative_image[i, j] = 255 - image[i, j]

    return negative_image

# Read the image in grayscale
image_path = 'lena.jpg' 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Manually invert the image
negative_image = manual_invert_image(image)

# Save the negative image
cv2.imwrite('negative.jpg', negative_image)

# Display the original and negative images
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
