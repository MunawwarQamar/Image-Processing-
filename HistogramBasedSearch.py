import cv2
import matplotlib.pyplot as plt

def crop_image(image, x, y, w, h):
    # Check if the input image is valid
    if image is None:
        print("Error: Unable to load the image.")
        return None

    # Crop the specified region from the image
    cropped_image = image[y:y+h, x:x+w]

    return cropped_image.astype('uint8')  # Convert the data type to uint8

# Read the grayscale image
grayscale_image = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image was read successfully
if grayscale_image is None:
    print("Error: Unable to read the image file. Please check the file path or file format.")
else:
    # Define the crop region (x, y, w, h)
    x = 200
    y = 200
    w = 200
    h = 100

    # Crop the image
    cropped_image = crop_image(grayscale_image, x, y, w, h)

    # Display the cropped image
    if cropped_image is not None:
        # Convert grayscale image to RGB for displaying with matplotlib
        original_image_rgb = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2RGB)
        
        # Draw rectangle around the cropped region on the original image
        cv2.rectangle(original_image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)  # BGR color format: (0, 255, 0) for green, thickness=2
        
        # Display the original image with the cropped region highlighted
        plt.imshow(original_image_rgb)
        plt.axis('off')  # Turn off axis
        plt.show()

      
