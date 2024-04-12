import cv2
import numpy as np

def manual_crop(image, x, y, w, h):
    # Initialize the cropped image array with zeros
    cropped_image = np.zeros((h, w), dtype=np.uint8)
    
    # Calculate the ending x and y coordinates
    end_x = x + w
    end_y = y + h
    
    # Iterating through the crop bounds
    for i in range(h):
        for j in range(w):
            # Map the coordinates to the original image
            orig_x = x + j
            orig_y = y + i
            if orig_y < image.shape[0] and orig_x < image.shape[1]:
                cropped_image[i, j] = image[orig_y, orig_x]
    
    return cropped_image

# Load an image in grayscale
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# Define the crop rectangle (x, y, width, height)
x, y, w, h = 200, 200, 200, 100  # Example values

# Crop the image
cropped_image = manual_crop(image, x, y, w, h)

# Save and show the cropped image
cv2.imwrite('cropped.jpg', cropped_image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
