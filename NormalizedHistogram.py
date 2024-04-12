import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_normalized_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the histogram manually
    hist = np.zeros(256)
    total_pixels = image.shape[0] * image.shape[1]

    # Iterate through each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            intensity = image[i, j]
            hist[intensity] += 1

    # Normalize the histogram to obtain probabilities
    hist_normalized = hist / total_pixels

    return hist_normalized

def plot_normalized_histogram(image_path):
    # Calculate the normalized histogram
    hist_normalized = calculate_normalized_histogram(image_path)

    # Plot the normalized histogram
    plt.plot(hist_normalized)
    plt.title("Normalized Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Probability")
    plt.show()

image_path = 'lena.jpg' 
plot_normalized_histogram(image_path)
