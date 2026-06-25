# 🤟 AI Sign Language Recognition System

An AI-powered Sign Language Recognition System that detects hand gestures using computer vision and deep learning, converts them into text, and provides audio output for better communication.

## 📌 Project Overview

This project helps bridge the communication gap between sign language users and non-sign language users by recognizing hand gestures in real-time using a trained deep learning model.

The system captures hand signs through a webcam, predicts the corresponding alphabet, displays the result on a web interface, and generates audio output.

---

## 🚀 Features

- Real-time hand gesture recognition
- Deep Learning based prediction model
- Webcam integration
- Text output for recognized signs
- Audio feedback using MP3 files
- User-friendly web interface
- Flask-based backend

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning & AI
- TensorFlow
- Keras
- NumPy
- OpenCV

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Other Tools
- Git
- GitHub

---

## 📂 Project Structure

AI_sign_language_system/
│
├── backend/
│ ├── app.py
│ ├── web_app.py
│ ├── templates/
│ │ └── index.html
│ └── audio/
│ ├── A.mp3
│ ├── B.mp3
│ └── ...
│
├── model/
│ └── sign_model.h5
│
├── training/
│ └── train_model.py
│
├── dataset/
│
├── requirements.txt
│
└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_sign_language_system.git
cd AI_sign_language_system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python backend/web_app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## 🧠 Model Training

To retrain the model:

```bash
python training/train_model.py
```

The trained model will be saved as:

```text
model/sign_model.h5
```

---

## 📸 Workflow

1. Capture hand gesture through webcam.
2. Preprocess image.
3. Pass image to trained model.
4. Predict sign language character.
5. Display recognized text.
6. Play corresponding audio output.

---

## 🎯 Future Enhancements

- Word prediction
- Sentence formation
- Support for Indian Sign Language (ISL)
- Mobile Application
- Multi-language voice output
- Cloud deployment

---

## 👨‍💻 Author

Praveen Kelim

DevOps & AI Enthusiast

---

## 📜 License

This project is created for educational and learning purposes.
