# Real-Time Face, Eye, and Smile Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/Computer%20vision-OpenCV-5C3EE8?logo=opencv&logoColor=white)
![Project type](https://img.shields.io/badge/Status-Learning%20demo-informational)

A webcam-based computer-vision demo using OpenCV Haar cascades to detect faces and inspect each detected face region for eyes and smiles.

## Detection flow

```mermaid
flowchart LR
    A[Webcam frame] --> B[Convert to grayscale]
    B --> C[Detect faces]
    C --> D[Inspect each face region]
    D --> E[Detect eyes and smiles]
    E --> F[Draw labels on frame]
```

## Included examples

| Script | Description |
| --- | --- |
| [FaceDetector.py](Face%26ObjectDetection/FaceDetector.py) | Face detection with a live camera preview |
| [Face_Eye_Smile_detector.py](Face%26ObjectDetection/Face_Eye_Smile_detector.py) | Face, eye, and smile detection in a live preview |

Both scripts use Haar cascade XML files bundled with the installed OpenCV Python package, so they do not depend on a machine-specific cascade path or the partial `EyeDetect.crdownload` file in the repository.

## Run locally

Install OpenCV in a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install opencv-python
```

On macOS or Linux, activate with `source .venv/bin/activate`.

From the repository root, run either example:

```powershell
python ".\Face&ObjectDetection\FaceDetector.py"
python ".\Face&ObjectDetection\Face_Eye_Smile_detector.py"
```

Allow the application to use the default camera. Press **q** in the preview window to quit. A desktop display is required for the OpenCV window.

## Limitations and privacy

- Haar-cascade detections are heuristic and may produce false positives or miss faces, eyes, and smiles under different lighting or camera conditions.
- This demo does not identify people and is not an identity-verification system.
- Frames are processed locally by the scripts and are not saved by this code.
