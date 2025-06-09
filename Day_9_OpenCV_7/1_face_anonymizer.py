
import mediapipe as mp
import cv2
import os

# human_image = cv2.imread(os.path.join(".","images","person_image.jpg")) #BGR Image

# # #resize
# resized_factor = 10
# width = int(human_image.shape[1] * resized_factor /100)
# height = int(human_image.shape[0] * resized_factor / 100)

# human_image = cv2.resize(human_image , (width , height))

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
  model_selection = 0,
  min_detection_confidence = 0.5
)

webcam = cv2.VideoCapture(0)

while True:
  _ , frame = webcam.read()
  
  height , width , _ = frame.shape
  result = face_detection.process(frame)
  
  if(result.detections is None):
    print("No Any Face Found")
    exit
  
  for detection in result.detections:
    bbox = detection.location_data.relative_bounding_box
    x = int(bbox.xmin * width)
    w = int(bbox.width * width)
  
    y = int(bbox.ymin * height)
    h = int(bbox.height * height)
  
  cropped_face = frame[y:y+h , x:x+w]
  blured_face = cv2.GaussianBlur(cropped_face,(51,51),0)
  frame[y:y+h,x:x+w] = blured_face
  cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
  cv2.imshow("Webcame",frame)
  
  if cv2.waitKey(4) & 0xFF == ord("q"):
    break

webcam.release()
cv2.destroyAllWindows()

# result = face_detection.process(human_image)

# # print(result.detections)

# height , width , _ = human_image.shape

# print(len(result.detections))
# print(type(result.detections))

# for detection in result.detections:
#   bbox = detection.location_data.relative_bounding_box
#   x = int(bbox.xmin * width)
#   w = int(bbox.width * width)
  
#   y = int(bbox.ymin * height)
#   h = int(bbox.height * height)
  
# cropped_face = human_image[y:y+h , x:x+w]
# blured_face = cv2.GaussianBlur(cropped_face,(51,51),0)
# human_image[y:y+h,x:x+w] = blured_face
# cv2.rectangle(human_image,(x,y),(x+w,y+h),(255,0,0),2)

# cv2.imshow("Cropped Face",human_image)
# cv2.waitKey(0)

# print(type(bbox))

