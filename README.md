# PPE-Vision-
# Real-Time PPE Detection System
<img width="1918" height="907" alt="Screenshot 2025-11-28 161022" src="https://github.com/user-attachments/assets/61d653e3-55d8-408c-84c6-779566f1823d" />

<img width="1856" height="911" alt="Screenshot 2025-11-28 161054" src="https://github.com/user-attachments/assets/ba2f38b3-9480-4338-8556-d02d1d19966c" />


## Project Overview
The Real-Time Personal Protective Equipment (PPE) Detection System is an AI-driven web application that monitors worker safety in real-time. The system detects PPE items such as helmets, safety vests, and gloves using computer vision (YOLOv8) and provides instant alerts for non-compliance. 

This project is built using **MERN stack (MongoDB, Express, React, Node.js)** for the web application and **Flask + YOLOv8** for real-time detection.

---


## Features

- **Real-Time PPE Detection:** Detects helmets, safety vests, gloves, and other safety gear using a webcam or IP camera.
- **User Authentication:** Secure login and registration using **MongoDB** with password hashing (`bcrypt`).
- **Live Webcam Streaming:** Smooth streaming pipeline using **OpenCV**.
- **Alerts:** Sends email notifications when PPE is missing.
- **Responsive UI:** Simple and user-friendly React frontend.
- **REST APIs:** Backend APIs for authentication and live detection.

---

## Tech Stack

- **Frontend:** React, HTML5, CSS3, JavaScript, Bootstrap
- **Backend:** Node.js, Express.js, Flask (for YOLO integration)
- **Database:** MongoDB (Mongoose ODM)
- **AI/ML:** YOLOv8, OpenCV
- **Other Tools:** Git, VS Code, Python, Jupyter Notebook

---

## Architecture

[React Frontend] <--HTTP--> [Express Backend] <--REST API--> [MongoDB]


[Flask Server with YOLOv8]
|
v
[Webcam / IP Camera]

yaml
Copy code

- Frontend communicates with Node.js backend through REST APIs.
- Flask server handles YOLO inference for PPE detection.
- MongoDB stores user data and authentication info.

---
Author:

Rajlaxmi Watgule – GitHub
 | LinkedIn

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Rajlaxmiwatgule2022bit059/ppe-detection.git
cd ppe-detection
2. Backend Setup
bash
Copy code
cd backend
npm install
Create .env file:

ini
Copy code
MONGO_URI=your_mongodb_connection_string
PORT=5000
Run the backend:

bash
Copy code
node index.js
3. Flask YOLO Server Setup
bash
Copy code
cd flask-server
pip install -r requirements.txt
Run Flask server:

bash
Copy code
python app.py
4. Frontend Setup
bash
Copy code
cd frontend
npm install
npm start
Access the app at http://localhost:3000.

Usage
Open the frontend in a browser.

Sign up or login as a user.

Navigate to the Live Detection page.

The system will access the webcam/IP camera, detect PPE in real-time, and display annotated frames.

If PPE is missing, an email alert will be sent automatically.

How It Works
Webcam Capture: Frames are captured using OpenCV.

YOLO Detection: Each frame is passed to YOLOv8 for PPE detection.

Annotation: Bounding boxes and labels are drawn on detected PPE items.

Real-Time Display: Annotated frames are displayed in the frontend.

Alert System: If PPE is missing for a certain period, email alerts are sent.

Data Model
User Schema (MongoDB):

Name: String

Email: String (unique)

Password: String (hashed)

Location: String

Date: Timestamp

YOLO Model:

Trained on images annotated with PPE classes

Evaluated using precision, recall, and mAP

Real-time inference for live video feeds

Key Optimizations
Latency Reduction: Frame resizing and lightweight YOLO model for faster processing.

Threading: Background threads handle email alerts without blocking detection.

Frontend Optimization: Efficient React rendering and minimal DOM updates.

Challenges Faced
Integrating MERN + Flask + YOLO smoothly.

Reducing real-time latency for live streaming.

Handling multi-threading for alerts without freezing the UI.

Debugging cross-technology errors between frontend, backend, and AI inference.

Future Enhancements
Support multiple camera streams simultaneously.

Add more PPE classes and anomaly detection.

Deploy on cloud for large-scale monitoring.

Mobile app integration for remote monitoring.


