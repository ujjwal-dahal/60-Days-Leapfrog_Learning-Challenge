
import os
import cv2

#reading image

image_path = os.path.join(".","image","doraemon.jpg")

image = cv2.imread(image_path)
print(image.shape)

cropped_image = image[100:580 , 250:650]


cv2.imshow("Cropped Image",cropped_image)
cv2.imshow("Original Image",image)
cv2.waitKey(0)