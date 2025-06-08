
import cv2
import numpy as np


# #Red Color ko Range
# # Red has two ranges in HSV

# # Lower red range
# lower_red1 = np.array([0, 100, 100])
# upper_red1 = np.array([10, 255, 255])

# # Upper red range
# lower_red2 = np.array([160, 100, 100])
# upper_red2 = np.array([180, 255, 255])

lower_blue = np.array([90, 50, 70])
upper_blue = np.array([128, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])



webcam = cv2.VideoCapture(0)

while True:
  ret , each_frame = webcam.read()
  
  
  #hsv ma convert garne
  frame_in_hsv = cv2.cvtColor(each_frame , cv2.COLOR_BGR2HSV)
  
  #masking garne -> esle chai eddi frame ma kunai object tyo lower ra upper range ko color paro bhane teslai white banaucha aru lai black
  # mask1 = cv2.inRange(frame_in_hsv , lower_red1 , upper_red1)
  # mask2 = cv2.inRange(frame_in_hsv , lower_red2 , upper_red2)
  
  # #combine mask
  # red_mask = cv2.bitwise_or(mask1 , mask2)
  
  
  '''Blue Masking'''
  blue_mask = cv2.inRange(frame_in_hsv , lower_blue , upper_blue)
  yellow_mask = cv2.inRange(frame_in_hsv , lower_yellow , upper_yellow)
  
  overall_mask = cv2.bitwise_or(blue_mask , yellow_mask)
  
  #abo red_mask ma contour apply garne
  contour , _ = cv2.findContours(overall_mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
  
  for cvt in contour:
    if cv2.contourArea(cvt) > 500:
      x , y , w , h = cv2.boundingRect(cvt)
      cv2.rectangle(each_frame , (x,y), (x+w,y+h),(0,255,0),2)
      
  cv2.imshow("Webcam",each_frame)
  # cv2.imshow("Masking",blue_mask)
  
  if cv2.waitKey(40) & 0xFF == ord("q"):
    break
  
  
webcam.release()
cv2.destroyAllWindows()
  
  
  
  
  