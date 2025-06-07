
import os
import cv2

#step1 : Load Image
bird_image = cv2.imread(os.path.join(".","images_","bird_image.png"))
bird_image = cv2.resize(bird_image , None , fx=0.5,fy=0.5)

#step 2 : GrayScale ma Convert
gray_scale_bird = cv2.cvtColor(bird_image,cv2.COLOR_BGR2GRAY)

#step 3 : Thresholding of Image
_ , image  = cv2.threshold(gray_scale_bird , 127 , 255 , cv2.THRESH_BINARY_INV)

#step 4 : finding contour
mode = cv2.RETR_EXTERNAL #Contour Retrieval Mode
method = cv2.CHAIN_APPROX_SIMPLE #Contour Approximation Method
contour , hierarchy = cv2.findContours(image , mode , method)

#step5 : Drawing Contour
contour_index = -1
color = (0,255,0)
thickness = 3
# cv2.drawContours(bird_image , contour, contour_index , color , thickness) #abo yo main image bird image ma contour apply huncha ani change ni gardincha tyo image lai automatically

for cvt in contour:
  if cv2.contourArea(cvt) > 50:
    x,y,w,h = cv2.boundingRect(cvt)
    cv2.rectangle(bird_image, (x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Bird Image",bird_image)
cv2.imshow("After Thresholding",image)
cv2.waitKey(0)
cv2.destroyAllWindows()