import os
import cv2

image_path = os.path.join(".","image","doraemon.jpg")
image = cv2.imread(image_path)

print(image.shape) #Output -> (height , width , channel)

scaled_percent = 30
width = int((image.shape[1] * scaled_percent)/100)
height = int((image.shape[0] * scaled_percent)/100)

resized_image = cv2.resize(image , (width,height)) #(width , height)
# resized_image = cv2.resize(image , (400,300)) #(width , height)

cv2.imwrite(os.path.join(".","image","resized_image.jpg"),resized_image)

cv2.imshow("Image",image)
cv2.imshow("Resized_image",resized_image)
cv2.waitKey(0)

