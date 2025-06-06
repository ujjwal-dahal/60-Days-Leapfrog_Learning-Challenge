import os
import cv2


image_path = os.path.join(".","images","image_for_thresholding.jpg")
image = cv2.imread(image_path)

scaled_percent = 80
width = int(image.shape[1] * scaled_percent / 100)
height = int(image.shape[0] * scaled_percent / 100)
image = cv2.resize(image , (width,height))


#suru ma Image lai grayscale ma convert garne
grayscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

#binary threshold -> esma pixel value > threshold_value then pixel_value = max_value else 0
#cv2.threshold(grayscale_image,threshold,max_value,type_of_threshold)
ret , binary_threshold = cv2.threshold(grayscale_image,80,255,cv2.THRESH_BINARY)
# cv2.imshow("Binary Threshold",binary_threshold)


handwritten = cv2.imread(os.path.join(".","images","handwritten.png"))
handwritten = cv2.cvtColor(handwritten,cv2.COLOR_BGR2GRAY)
cv2.imshow("Handwritten",handwritten)
handwritten_threshold = cv2.adaptiveThreshold(handwritten,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY,21,10)
cv2.imshow("Inverse Binary Threshold",handwritten_threshold)


# cv2.imshow("Original Image",image)
# cv2.imshow("GrayScale Image",grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

