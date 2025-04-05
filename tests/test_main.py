import pytest
import cv2
import numpy as np
from src.main import AutonomousDrivingSystem

def test_system_initialization():
    """Test if the system initializes correctly"""
    ads = AutonomousDrivingSystem()
    assert ads is not None
    assert hasattr(ads, 'object_detector')
    assert hasattr(ads, 'lane_detector')
    assert hasattr(ads, 'pedestrian_detector')
    assert hasattr(ads, 'navigator')

def test_frame_processing():
    """Test if frame processing works"""
    ads = AutonomousDrivingSystem()
    # Create a dummy frame
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    processed_frame = ads.process_frame(frame)
    assert processed_frame is not None
    assert isinstance(processed_frame, np.ndarray)
    assert processed_frame.shape == frame.shape

def test_visualization():
    """Test if visualization works"""
    ads = AutonomousDrivingSystem()
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    objects = []
    lanes = []
    pedestrians = []
    path = []
    visualized_frame = ads.visualize_results(frame, objects, lanes, pedestrians, path)
    assert visualized_frame is not None
    assert isinstance(visualized_frame, np.ndarray)
    assert visualized_frame.shape == frame.shape 