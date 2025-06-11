
from ultralytics import YOLO
import os


#already trained bhayeko model import garne Either yolov8n.pt OR yolo11n.pt
model = YOLO("yolo11n.pt")

results = model(os.path.join(".","test_videos","tiger_zebra.mp4"),save=True)
