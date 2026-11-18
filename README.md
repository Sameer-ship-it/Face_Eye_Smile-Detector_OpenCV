# Real-Time Face, Eye, and Smile Detection

A small Python computer-vision demo that detects faces, eyes, and smiles in webcam frames using OpenCV Haar cascade classifiers.

## Features

- Live webcam capture
- Face detection with eye and smile detection within each face
- Included Haar cascade XML files
- A separate face-detection example

## Repository layout

```text
Face&ObjectDetection/
├── FaceDetector.py
├── Face_Eye_Smile_detector.py
├── haarcascade_frontalface_default.xml
└── haarcascade_smile.xml
```

## Run locally

```bash
git clone https://github.com/Sameer-ship-it/Face_Eye_Smile-Detector_OpenCV.git
cd Face_Eye_Smile-Detector_OpenCV
python -m venv .venv
```

Activate the environment and install OpenCV:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

```bash
python -m pip install opencv-python
python Face&ObjectDetection/Face_Eye_Smile_detector.py
```

The scripts need a working webcam. Press `q` in the video window to exit. If the cascade files cannot be found, run the script from the `Face&ObjectDetection` directory:

```bash
cd Face&ObjectDetection
python Face_Eye_Smile_detector.py
```

## How it works

Each frame is converted to grayscale, then passed through the included Haar cascades. The face detector identifies regions of interest; the eye and smile detectors run within those regions. Results are drawn on the live frame.

## Scope and limitations

Haar cascades are lightweight classical detectors. Results vary with lighting, camera quality, pose, and face orientation; this is a demonstration rather than a biometric or identity system.

## Author

[Sameer Raza](https://github.com/Sameer-ship-it)
