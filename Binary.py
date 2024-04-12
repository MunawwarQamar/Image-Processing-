import cv2

# Read the original image
image = cv2.imread("lena.jpg") 

# Convert the image to grayscale (if colored)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create the binary image
# You can adjust the threshold value (127) based on your image
ret, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the original and binary images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary_image)
cv2.imwrite('binary.jpg', binary_image)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()


