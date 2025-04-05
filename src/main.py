import cv2
import numpy as np
from object_detection.detector import ObjectDetector
from lane_tracking.lane_detector import LaneDetector
from pedestrian_recognition.pedestrian_detector import PedestrianDetector
from route_planning.navigator import Navigator

class AutonomousDrivingSystem:
    def __init__(self):
        self.object_detector = ObjectDetector()
        self.lane_detector = LaneDetector()
        self.pedestrian_detector = PedestrianDetector()
        self.navigator = Navigator()
        
    def process_frame(self, frame):
        # Object detection
        objects = self.object_detector.detect(frame)
        
        # Lane detection
        lanes = self.lane_detector.detect(frame)
        
        # Pedestrian detection
        pedestrians = self.pedestrian_detector.detect(frame)
        
        # Route planning
        path = self.navigator.plan_route(objects, lanes, pedestrians)
        
        # Visualize results
        self.visualize_results(frame, objects, lanes, pedestrians, path)
        
        return frame
    
    def visualize_results(self, frame, objects, lanes, pedestrians, path):
        # Draw detected objects
        for obj in objects:
            x1, y1, x2, y2, conf, cls = obj
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{cls}: {conf:.2f}', (x1, y1-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Draw lanes
        for lane in lanes:
            cv2.polylines(frame, [lane], False, (0, 0, 255), 2)
        
        # Draw pedestrians
        for ped in pedestrians:
            x1, y1, x2, y2, conf = ped
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f'Pedestrian: {conf:.2f}', (x1, y1-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # Draw planned path
        if path:
            cv2.polylines(frame, [np.array(path)], False, (255, 255, 0), 2)

def main():
    # Initialize the autonomous driving system
    ads = AutonomousDrivingSystem()
    
    # Open video capture (0 for webcam, or video file path)
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process the frame
        processed_frame = ads.process_frame(frame)
        
        # Display the result
        cv2.imshow('Autonomous Driving System', processed_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main() 