# Facial Recognition System using OpenCV

This project implements a simple facial recognition system using `OpenCV` for real-time video capture and the `face_recognition` library for facial matching. The system compares faces detected from the camera feed with a reference image (`dni.jpg`), highlighting a match with a green rectangle and a mismatch with a red rectangle.

## Features

- **Face Detection**: Detects faces in real-time using your webcam.
- **Face Recognition**: Compares detected faces with a reference image (`dni.jpg`).
- **Real-time Video Processing**: Processes video frames from the webcam and displays the result with a simple overlay showing match or no match.

## Requirements

Make sure you have the following Python libraries installed:

- `opencv-python`
- `face_recognition`
- `numpy`

You can install them using pip:

```bash
pip install opencv-python face_recognition numpy
```
