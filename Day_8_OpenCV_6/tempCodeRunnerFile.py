import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
  _ , frame = webcam.read()

  gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
  
  faces = face_cascade.detectMultiScale(gray_frame , scaleFactor=1.1 , minNeighbors=5)
  
  for (x,y,w,h) in faces:
    cv2.rectangle(frame , (x,y),(x+w,y+h),(255,255,255)0.1)
    cropped_face = frame[y:y+h,x:x+w]
    blur_part = cv2.GaussianBlur(cropped_face,(51,51),0)
    
    frame[y:y+h,x:x+w] = blur_part
  
  cv2.imshow("Webcame",frame)
  if cv2.waitKey(4) & 0xFF == ord("q"):
    break
  

webcam.release()
cv2.destroyAllWindows()
