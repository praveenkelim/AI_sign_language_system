from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import os
import time
from tensorflow.keras.models import load_model
import mediapipe as mp

app = Flask(__name__)

model = load_model("../model/sign_model.h5")

TRAIN_PATH = "../dataset/asl_alphabet_train"
labels = sorted(os.listdir(TRAIN_PATH))

IMG_SIZE = 64

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# MediaPipe Setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# Global states
latest_prediction = {
    "gesture": "none",
    "confidence": 0.0,
    "fps": 0,
    "history": [],
    "hand_detected": False
}

prev_time = 0
history = []
last_added = ""

def generate_frames():
    global latest_prediction, prev_time, history, last_added

    while True:
        success, frame = camera.read()
        if not success:
            break

        # FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time
        fps = int(fps)

        frame = cv2.flip(frame, 1)

        # ROI Box
        x1, y1 = 50, 50
        x2, y2 = 350, 350

        # --- MediaPipe Hand Detection ---
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        hand_present = False

        if results.multi_hand_landmarks:
            hand_present = True
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        # --- CNN Prediction ---
        roi = frame[y1:y2, x1:x2]
        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        roi_resized = cv2.resize(roi_rgb, (IMG_SIZE, IMG_SIZE))
        roi_resized = roi_resized / 255.0
        roi_input = np.reshape(roi_resized, (1, IMG_SIZE, IMG_SIZE, 3))

        prediction = model.predict(roi_input, verbose=0)
        class_id = int(np.argmax(prediction))
        gesture = labels[class_id]
        confidence = float(np.max(prediction))

        # History Logic
        if confidence > 0.60:
            if gesture != last_added and gesture not in ["nothing", "space", "del"]:
                history.append(gesture)
                last_added = gesture
                if len(history) > 5:
                    history.pop(0)

        latest_prediction = {
            "gesture": gesture,
            "confidence": confidence,
            "fps": fps,
            "history": history,
            "hand_detected": hand_present
        }

        # Draw ROI Box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video")
def video():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/prediction")
def prediction():
    return jsonify(latest_prediction)

if __name__ == "__main__":
    app.run(debug=False, threaded=True)