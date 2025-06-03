
import cv2

webcam = cv2.VideoCapture(0) #eddi computer ma euta matra webcam cha bhane 0 dine 
#multiple webcam cha bhane tai anusar number dine

#visualize webcam

while True:
  ret , frame = webcam.read()
  
  cv2.imshow("webcame_frame",frame)
  if cv2.waitKey(40) & 0xFF == ord("q"):
    break
  
webcam.release()
cv2.destroyAllWindows()