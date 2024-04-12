import cv2
import numpy as np
def image_entropy(image):
    # Calculate histogram
    hist = cv2.calcHist([image], [0], None, [256], [0,256])
    # Check for zero sum (uniform image or empty image)
    if np.sum(hist) == 0:
        return 0
    # Normalize histogram
    hist /= hist.sum()
    # Calculate entropy
    entropy = -np.sum(hist * np.log2(hist + 1e-10))  # Adding a small value to avoid log(0)
    return entropy

image_path = 'lena.jpg' 
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
entropy_value = image_entropy(gray_image)
print("Entropy of the image is:" ,entropy_value)