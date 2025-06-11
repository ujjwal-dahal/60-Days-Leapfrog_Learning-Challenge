
from ultralytics import YOLO
import os 


#pretrained model load gareko
model = YOLO("yolov8n.pt")  #n means nano & lightweight

#single image detect
results = model(os.path.join(".","images","dog_cat.jpg"))


# print(type(results))
results[0].show() #esle object classify bhaesi tesko result dekhaucha

#classify bhaeko image lai save garna
results[0].save(filename=os.path.join(".","output_images","dog_cat_output.jpg"))