"""Detect faces, eyes, and smiles from the default webcam using Haar cascades."""

import cv2


def load_cascade(filename):
    path = cv2.data.haarcascades + filename
    classifier = cv2.CascadeClassifier(path)
    if classifier.empty():
        raise FileNotFoundError(f"Could not load OpenCV cascade: {path}")
    return classifier


def main():
    face_cascade = load_cascade("haarcascade_frontalface_default.xml")
    eye_cascade = load_cascade("haarcascade_eye.xml")
    smile_cascade = load_cascade("haarcascade_smile.xml")

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError("Could not open the default camera (device 0).")

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, width, height) in faces:
                face_gray = gray[y:y + height, x:x + width]
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

                eyes = eye_cascade.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=10)
                smiles = smile_cascade.detectMultiScale(face_gray, scaleFactor=1.7, minNeighbors=20)

                if len(eyes) > 0:
                    cv2.putText(frame, "Eyes detected", (x, max(y - 30, 20)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
                if len(smiles) > 0:
                    cv2.putText(frame, "Smile detected", (x, max(y - 10, 20)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

            cv2.imshow("Face, Eye, and Smile Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
