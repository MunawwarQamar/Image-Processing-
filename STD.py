import cv2
import numpy as np

def calculateStandardDeviation(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale if it's a color image
    if len(image.shape) > 2 and image.shape[2] > 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the mean intensity value of the image
    mean_intensity = np.mean(image)

    # Calculate the squared differences from the mean for each pixel
    squared_diffs = (image - mean_intensity) ** 2

    # Calculate the sum of squared differences
    sum_squared_diffs = np.sum(squared_diffs)

    # Calculate the total number of pixels
    total_pixels = image.shape[0] * image.shape[1]

    # Calculate the variance
    variance = sum_squared_diffs / total_pixels

    # Calculate the standard deviation (square root of variance)
    standard_deviation = np.sqrt(variance)

    return standard_deviation

image_path = 'lena.jpg' 
std_dev = calculateStandardDeviation(image_path)
print("Standard Deviation of the image is:", std_dev)
