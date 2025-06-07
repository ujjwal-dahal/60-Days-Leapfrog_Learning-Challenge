
import cv2
import os

webcame = cv2.VideoCapture(0)

ret = True
while True:
  ret , frame = webcame.read()
  
  grayscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  
  _ , threshold_frame = cv2.threshold(grayscale_frame , 127 , 255 , cv2.THRESH_BINARY_INV)
  
  contour , hierarchy = cv2.findContours(threshold_frame  ,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  
  for cvt in contour:
    if cv2.contourArea(cvt) > 500:
      x,y,w,h = cv2.boundingRect(cvt)
      cv2.rectangle(frame , (x,y),(x+w,y+h),(0,255,0),2)
  
  cv2.imshow("Webcamera",frame)
  
  if cv2.waitKey(20) & 0xFF == ord("q"):
    break
  

  