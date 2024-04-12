import cv2
import numpy as np

def apply_blur_filter(image, kernel_size=3):
    # Ensure the kernel size is odd to have a central pixel
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size should be odd")

    # Pad the image to handle the borders
    pad_width = kernel_size // 2
    padded_image = np.pad(image, pad_width, mode='constant', constant_values=0)

    # Prepare the output image
    blurred_image = np.zeros_like(image)

    # Get the dimensions of the image
    rows, cols = image.shape

    # Apply the averaging filter
    for i in range(rows):
        for j in range(cols):
            # Extract the region of interest
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            # Calculate the average and assign it to the blurred image
            blurred_image[i, j] = np.mean(region)

    return blurred_image

# Read the image in grayscale
image_path = 'lena.jpg'  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply the blur filter
blurred_image = apply_blur_filter(image, kernel_size=3)  # You can change the kernel size to increase blur

# Save the blurred image
cv2.imwrite('blurred.jpg', blurred_image)

# Display the images 
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
