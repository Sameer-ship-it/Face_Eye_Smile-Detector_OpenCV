# 😃 Real-Time Face, Eye & Smile Detector

A fun little Computer Vision project that detects **faces 👤, eyes 👀, and smiles 😁** in real time using your webcam — powered by **OpenCV** and classic **Haar Cascade Classifiers**.

No deep learning, no GPU, no heavy setup — just pure classical CV magic running live on your screen! ✨

---

## 🎥 What It Does

Point your webcam at yourself (or a friend 👋) and watch the magic happen:

- 🟩 Draws a box around every **face** it detects
- 🔵 Spots **eyes** within each face
- 🟡 Catches that **smile** the moment you flash it

All of this happens **frame-by-frame, in real time** — no lag, no fuss.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core language |
| 📷 OpenCV | Image processing & video capture |
| 🌳 Haar Cascades | Pre-trained classifiers for face/eye/smile detection |

---

## 📂 Project Structure

```
📁 Face_Eye_Smile_Detector
├── FaceDetector.py                        # Standalone face detection script
├── Face_Eye_Smile_detector.py             # Main script — detects face + eyes + smile
├── haarcascade_frontalface_default.xml    # Pre-trained face detection model
├── haarcascade_smile.xml                  # Pre-trained smile detection model
└── README.md                              # You're reading it! 👋
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Sameer-ship-it/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install the dependencies
```bash
pip install opencv-python
```

### 3️⃣ Run it! 🎬
```bash
python Face_Eye_Smile_detector.py
```

📸 Your webcam will fire up — smile at the camera and watch it get detected live!
Press **`q`** to quit anytime.

---

## ⚙️ How It Works

1. 🎥 Captures live video from your webcam using `cv2.VideoCapture()`
2. 🖤 Converts each frame to grayscale (Haar Cascades work best in grayscale)
3. 🔍 Runs the **face cascade** to locate faces
4. 👀 Within each detected face, runs the **eye cascade**
5. 😁 Runs the **smile cascade** to catch that grin
6. 🟩 Draws rectangles around all detections on the live video feed

---

## 💡 Why This Project?

This was built to get **hands-on with classical Computer Vision techniques** — understanding how detection worked *before* deep learning took over, and appreciating how well Haar Cascades still perform for lightweight, real-time tasks. 🧠⚡

---

## 🔮 Future Improvements

- [ ] Add emotion detection 😢😠😄
- [ ] Switch to a DNN-based face detector for better accuracy
- [ ] Add face-count / smile-count on-screen stats
- [ ] Deploy as a simple web app using Streamlit

---

## 🙌 Connect With Me

- 💻 GitHub: [Sameer-ship-it](https://github.com/Sameer-ship-it)
- 🔗 LinkedIn: [sameerraza](https://linkedin.com/in/sameerraza)
- 📧 Email: draza8757@gmail.com

---

⭐ If you liked this project, don't forget to **star the repo**! It keeps the motivation going 🚀
