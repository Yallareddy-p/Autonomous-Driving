import torch
import cv2
import numpy as np

class ObjectDetector:
    def __init__(self, model_path='yolov5s.pt'):
        # Load YOLOv5 model
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.conf = 0.5  # Confidence threshold
        self.model.iou = 0.45  # NMS IoU threshold
        
    def detect(self, frame):
        # Convert frame to RGB (YOLOv5 expects RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Perform detection
        results = self.model(frame_rgb)
        
        # Process results
        detections = []
        for *xyxy, conf, cls in results.xyxy[0]:
            x1, y1, x2, y2 = map(int, xyxy)
            detections.append([x1, y1, x2, y2, float(conf), self.model.names[int(cls)]])
            
        return detections 