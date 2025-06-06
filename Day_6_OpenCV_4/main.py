import os
import cv2
import numpy as np

image = cv2.imread(os.path.join(".","testing_images","player_image.jpeg"))
image = cv2.resize(image , None , fx=0.4,fy=0.4)

canny_image = cv2.Canny(image , 100 , 200)
#100 is Threshold1 i.e Low Bound
#200 is Threshold2 i.e High Bound
#-> Pixel Ko Value 100 Bhanda Low huda It will be Ignore
#-> Pixel ko Value 200 Bhanda High huda It will be Strong Edge
#-> Pixel ko Value 100 & 200 ko Between Lie garda It will be Weak Edge.

#dilet le white edge ko thickness lai bold banaucha ajai
#kernel ko size either 3x3 huncha or 5x5
kernel = np.ones((3,3),np.uint8)
dilet_image = cv2.dilate(canny_image,kernel)

#erosion is oppsoite of dilet
erosion_image = cv2.erode(dilet_image,kernel)

cv2.imshow("Plyer Image",image)
cv2.imshow("Canny Edge Detection",canny_image)
cv2.imshow("Dilet Image",dilet_image)
cv2.imshow("Erosion Image",erosion_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

