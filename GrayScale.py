import numpy as np
import matplotlib.pyplot as plt
import cv2



image = plt.imread("lena.jpg")
def img2gray(img):
    # r,g,b=img[...,0],img[...,1],img[...,2]#red in zero , green in one , blue in two # ... -> that mean that i dont care about the previous acssess
    # gray =0.229*r +0.587*g +0.114*b # this number give the best result to convert to gray scale and its populer
   gray =  np.dot(img[...,0:3],[0.229,0.587,0.114])
   return gray


grayImage=img2gray(image)
cv2.imwrite('grayscale.jpg', grayImage)  # Save the gray image
plt.imshow(grayImage,cmap="gray")
plt.show()

