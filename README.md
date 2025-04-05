# Autonomous Driving System 🚗

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/Yallareddy-p/Autonomous-Driving/actions/workflows/tests.yml/badge.svg)](https://github.com/Yallareddy-p/Autonomous-Driving/actions/workflows/tests.yml)

## Overview

An autonomous driving system implementing computer vision and AI for:
- Real-time object detection
- Lane tracking
- Pedestrian recognition
- Route planning

## Features

- 🎯 **Object Detection**: YOLOv5-based real-time object detection
- 🛣️ **Lane Tracking**: Computer vision-based lane detection
- 👥 **Pedestrian Recognition**: HOG-based pedestrian detection
- 🗺️ **Route Planning**: A* algorithm for path planning
- 🎨 **Real-time Visualization**: Live feed with detection overlays

## Installation

### Prerequisites

- Python 3.8+
- CUDA-capable GPU (optional, for better performance)
- Webcam or video input device

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Yallareddy-p/Autonomous-Driving.git
cd Autonomous-Driving
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download YOLOv5 model:
```bash
python -c "import torch; torch.hub.load('ultralytics/yolov5', 'yolov5s')"
```

## Usage

Run the main application:
```bash
python src/main.py
```

### Controls
- Press 'q' to quit
- Press 's' to save current frame
- Press 'p' to pause/resume

## Project Structure

```
autonomous-driving/
├── src/                    # Source code
│   ├── main.py            # Main application
│   ├── object_detection/  # Object detection module
│   ├── lane_tracking/     # Lane detection module
│   ├── pedestrian_recognition/  # Pedestrian detection
│   └── route_planning/    # Path planning module
├── tests/                 # Test files
├── docs/                  # Documentation
├── data/                  # Sample data
├── models/               # Trained models
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Development

### Code Style
We use Black for code formatting:
```bash
pip install black
black .
```

### Testing
Run tests:
```bash
python -m pytest tests/
```

### Documentation
Generate documentation:
```bash
cd docs
make html
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLOv5 team for the object detection model
- OpenCV community for computer vision tools
- Contributors and maintainers

## Contact

Yallareddy P - [@Yallareddy-p](https://github.com/Yallareddy-p)

Project Link: [https://github.com/Yallareddy-p/Autonomous-Driving](https://github.com/Yallareddy-p/Autonomous-Driving) 