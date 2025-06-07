import os
import cv2


#load image
animals_image = cv2.imread(os.path.join(".","images_","animal.jpg"))

#convert bgr image into grayscale image
grayscale_image = cv2.cvtColor(animals_image, cv2.COLOR_BGR2GRAY)

#threshold that image i.e convert to black & white
_ , threshold_image = cv2.threshold(grayscale_image, 115 , 255 , cv2.THRESH_BINARY_INV)

#create counter
contour_for_image , _ = cv2.findContours(threshold_image , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

#remove noise
for cvt in contour_for_image:
  print(cv2.contourArea(cvt))
  if cv2.contourArea(cvt) > 400:
    x , y , w ,h = cv2.boundingRect(cvt)
    cv2.rectangle(animals_image,(x,y), (x+w , y + h) , (0,0,255),2)



#show image
# cv2.imshow("Threshold Image",threshold_image)
cv2.imshow("Counter Image",animals_image)
cv2.waitKey(0)
cv2.destroyAllWindows()