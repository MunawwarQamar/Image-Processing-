import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_cumulative_histogram(image_path):
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

    # Compute the cumulative histogram manually
    cumulative_hist = np.zeros(256)
    cumulative_sum = 0
    for i in range(256):
        cumulative_sum += hist[i]
        cumulative_hist[i] = cumulative_sum

    # Normalize the cumulative histogram
    cumulative_hist_normalized = cumulative_hist / total_pixels

    return cumulative_hist_normalized

def plot_cumulative_histogram(image_path):
    # Calculate the cumulative histogram
    cumulative_hist_normalized = calculate_cumulative_histogram(image_path)

    # Plot the cumulative histogram
    plt.plot(cumulative_hist_normalized)
    plt.title("Cumulative Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Cumulative Probability")
    plt.show()

image_path = 'lena.jpg'  
plot_cumulative_histogram(image_path)
