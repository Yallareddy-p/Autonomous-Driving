import cv2
import numpy as np

class PedestrianDetector:
    def __init__(self):
        # Load HOG descriptor and SVM classifier for pedestrian detection
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        
    def detect(self, frame):
        # Detect pedestrians in the frame
        boxes, weights = self.hog.detectMultiScale(frame, winStride=(4, 4),
                                                 padding=(8, 8), scale=1.05)
        
        # Process detections
        pedestrians = []
        for (x, y, w, h), weight in zip(boxes, weights):
            pedestrians.append([x, y, x + w, y + h, float(weight)])
            
        return pedestrians 