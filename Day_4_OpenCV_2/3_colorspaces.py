
import os
import cv2

image_path = os.path.join(".","image","doraemon.jpg")

#read image
image = cv2.imread(image_path) #esle abo numpy array dincha image lai read garera

grayscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY) #esle BGR Image lai Grayscale image ma convert garcha

hsl_image = cv2.cvtColor(image , cv2.COLOR_BGR2HLS)

rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

hsv_image = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)


# grayscale_image = cv2.imread(os.path.join(".","image","rose_grayscale_image.jpg"),cv2.IMREAD_GRAYSCALE)
# gray_to_bgr = cv2.cvtColor(grayscale_image,cv2.COLOR_GRAY2RGB)


# scaled_percent = 10
# width = int((gray_to_bgr.shape[1] * scaled_percent)/100)
# height = int((gray_to_bgr.shape[0] * scaled_percent)/100)
# resized_grayscale_image = cv2.resize(gray_to_bgr,(width,height))

#BGR image to RGB garda Blue Convert to Red ani Red -> Blue huncha
#visualize image
# cv2.imshow("Visualize Image",image)
# cv2.imshow("HSL Image",hsl_image) 
# cv2.imshow("Grayscale Image",grayscale_image)
# cv2.imshow("RGB Image",rgb_image)

# cv2.imshow("GrayScale Image to BGR Image",resized_grayscale_image)
cv2.imshow("HSV Image",hsv_image)

cv2.waitKey(0)  
cv2.destroyAllWindows()