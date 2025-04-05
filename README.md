# Autonomous Driving System

This project implements an autonomous driving system with the following key components:

1. Object Detection - Using YOLOv5 for real-time object detection
2. Lane Tracking - Computer vision-based lane detection and tracking
3. Pedestrian Recognition - Specialized detection for pedestrians
4. Route Planning - Path planning and navigation

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main application:
```bash
python src/main.py
```

## Project Structure

- `src/` - Main source code
  - `object_detection/` - Object detection module
  - `lane_tracking/` - Lane detection and tracking
  - `pedestrian_recognition/` - Pedestrian detection
  - `route_planning/` - Path planning and navigation
  - `utils/` - Utility functions
- `models/` - Pre-trained models
- `data/` - Training and test data
- `tests/` - Test files 