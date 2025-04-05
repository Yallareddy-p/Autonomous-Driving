import cv2
import numpy as np

class LaneDetector:
    def __init__(self):
        # Parameters for lane detection
        self.kernel_size = 5
        self.low_threshold = 50
        self.high_threshold = 150
        self.rho = 2
        self.theta = np.pi/180
        self.threshold = 15
        self.min_line_length = 40
        self.max_line_gap = 20
        
    def detect(self, frame):
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur
        blur_gray = cv2.GaussianBlur(gray, (self.kernel_size, self.kernel_size), 0)
        
        # Apply Canny edge detection
        edges = cv2.Canny(blur_gray, self.low_threshold, self.high_threshold)
        
        # Create a mask for the region of interest (ROI)
        height, width = frame.shape[:2]
        mask = np.zeros_like(edges)
        vertices = np.array([[(0, height), (width/2, height/2), (width, height)]], dtype=np.int32)
        cv2.fillPoly(mask, vertices, 255)
        masked_edges = cv2.bitwise_and(edges, mask)
        
        # Apply Hough transform to detect lines
        lines = cv2.HoughLinesP(masked_edges, self.rho, self.theta, self.threshold,
                               np.array([]), self.min_line_length, self.max_line_gap)
        
        # Process detected lines
        lanes = []
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                lanes.append(np.array([[x1, y1], [x2, y2]], dtype=np.int32))
                
        return lanes 