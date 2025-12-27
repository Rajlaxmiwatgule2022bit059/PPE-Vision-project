import os
import subprocess
import threading
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  
def run_detection():
    try:
        # ✅ Correct absolute path to your detection folder
        project_path = r"C:\Users\sunil\OneDrive\Desktop\PPE-vision\detection\Construction-PPE-detection-main"
        script_path = os.path.join(project_path, "webcam.py")  # 👈 detection script

        print(f"🔍 Running detection script at: {script_path}")

        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Could not find {script_path}")

        # ✅ Run the script in its directory
        subprocess.run(
            ["python", "webcam.py"],
            cwd=project_path,
            check=True
        )

    except Exception as e:
        print(f"❌ Error while starting detection: {e}")

@app.route("/start-detection")
def start_detection():
    thread = threading.Thread(target=run_detection)
    thread.start()
    return jsonify({"status": "Detection started"}), 200

@app.route("/")
def home():
    return jsonify({"message": "Backend running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
