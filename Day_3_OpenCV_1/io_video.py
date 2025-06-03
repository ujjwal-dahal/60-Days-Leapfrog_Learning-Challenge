
import os
import cv2


#read video
video_path = os.path.join(".","video","ant.mp4")

video = cv2.VideoCapture(video_path)


#visualize video

ret = True

while ret:
  ret , frame = video.read() #esle two variable return garcha
  #video.read() le frame ra ret return garcha ret is Boolean Value ho which means it becomes false jaba frame sakincha
  #ret is True until frame finishes
  
  if ret:
  
    cv2.imshow("video_title",frame)
    
    cv2.waitKey(40)
    #since video is made up of frame so openCV le each 40 Milisecond ma each frame dekhaucha
    
video.release() #openCV le video complete bhaesi memory release garcha jun esle allocate gareko huncha suru ma -> video object le

cv2.destroyAllWindows()