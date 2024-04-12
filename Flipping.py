import cv2
import numpy as np

def flip_horizontally(image):
    # Create an empty array with the same shape as the input image
    flipped_image = np.zeros_like(image)
    
    # Get the number of columns in the image
    cols = image.shape[1]
    
    # Flip each column by reversing the order
    for i in range(cols):
        flipped_image[:, i] = image[:, cols - 1 - i]
    
    return flipped_image

# Load an image in grayscale
image_path = 'lena.jpg' 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply the manual horizontal flip
flipped_image = flip_horizontally(image)

# Save the flipped image
cv2.imwrite('flipped.jpg', flipped_image)

# If you want to display the images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
