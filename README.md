# Facial Recognition System using OpenCV

This project implements a simple facial recognition system using `OpenCV` for real-time video capture and the `face_recognition` library for facial matching. The system is specifically designed to compare faces detected from the camera feed with a reference image of a Spanish **DNI (Documento Nacional de Identidad)**, highlighting a match with a green rectangle and a mismatch with a red rectangle.

## Features

- **Face Detection**: Detects faces in real-time using your webcam.
- **Face Recognition**: Compares detected faces with a reference image (`dni.jpg`), particularly useful for verifying Spanish DNIs.
- **Real-time Video Processing**: Processes video frames from the webcam and displays the result with an overlay showing match or no match.
- **DNI Verification**: This project is designed for biometric verification using the Spanish DNI, making it ideal for use cases where document validation is required.

## Requirements

Make sure you have the following Python libraries installed:

- `opencv-python`
- `face_recognition`
- `numpy`

You can install them using pip:

```bash
pip install opencv-python face_recognition numpy
```
## Biometric Use Cases

This system can be used in various biometric applications, particularly those involving Spanish identification documents:

- **Access Control**: Verify the identity of individuals using their DNI to grant or deny access to restricted areas or systems.
- **Document Verification**: Compare the face on the DNI with the person presenting it to ensure the document matches the individual.
- **Attendance Systems**: Use face recognition with Spanish DNIs to automatically log attendance in workplaces, schools, or events.
- **Security Applications**: Enhance security systems by incorporating DNI-based face recognition to identify individuals in sensitive locations or public places.
- **Customer Verification**: Financial institutions and other businesses can use this system to validate the identity of their customers through their DNI for secure transactions or services.

