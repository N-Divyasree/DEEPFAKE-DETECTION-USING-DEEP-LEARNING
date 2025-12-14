from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from model import predict

app = Flask(_name_)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Deepfake Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict_api():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = predict(file_path)

    # Return flat JSON
    return jsonify(result)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)