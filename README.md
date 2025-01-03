# HueWatch

A real-time color detection system built with OpenCV that identifies and tracks colors from your webcam feed. This tool provides instant color recognition with live bounding box visualization.

## Features
- Real-time color detection using webcam feed
- Support for multiple basic colors (red, blue, green, purple, yellow, etc.)
- Dynamic bounding box visualization around detected colors
- Noise reduction through contour area filtering
- Simple command-line interface for color selection

## Installing Required Packages
pip install -r requirements.txt

## Usage
- Run the main script
  - python main.py
- Enter the color you want to detect when prompted on command-line (e.g., "blue", "red", "green")
- A window will open showing your webcam feed with bounding boxes around detected colors
- Press 'q' to quit the program
- 
## File Structure
HueWatch/
├── main.py          # Main script for color detection
├── helper.py        # Helper functions for color range calculation
├── requirements.txt # Required packages
└── README.md       # Project documentation

## Acknowldgements
- Built with OpenCV
- Part of my learning journey in computer vision and Python development
- Project created to understand real-time color detection and image processing fundamentals
- Inspired by computer vision applications in real-time color tracking
