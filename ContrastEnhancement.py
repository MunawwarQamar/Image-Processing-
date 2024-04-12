import cv2
import numpy as np

def enhance_contrast(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the histogram of the image
    hist, _ = np.histogram(image.flatten(), 256, [0,256])

    # Calculate the cumulative distribution function (CDF) of the histogram
    cdf = hist.cumsum()
    
    # Normalize the CDF to a range of [0,255]
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    
    # Interpolate the CDF to get the equalized pixel values
    equalized_image = np.interp(image.flatten(), range(256), cdf_normalized).reshape(image.shape).astype(np.uint8)

    # Save the enhanced image
    output_path = image_path.replace('lena.', 'contrast-enhanced.')
    cv2.imwrite(output_path, equalized_image)

    return output_path

image_path = 'lena.jpg'  
enhanced_image_path = enhance_contrast(image_path)
print("Enhanced image saved as:", enhanced_image_path)
