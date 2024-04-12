import cv2

def calculateMean(image_path):
    # Read the image 
    image = cv2.imread(image_path)

    # Convert the image to grayscale if it's a color image
    if len(image.shape) > 2 and image.shape[2] > 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the sum of pixel values and count of pixels
    sum_pixels = 0
    total_pixels = image.shape[0] * image.shape[1]

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            sum_pixels += image[i, j]

    # Calculate the mean
    mean_value = sum_pixels / total_pixels

    return mean_value

image_path = 'lena.jpg' 
mean = calculateMean(image_path)
print("Mean of the image is:", mean)
